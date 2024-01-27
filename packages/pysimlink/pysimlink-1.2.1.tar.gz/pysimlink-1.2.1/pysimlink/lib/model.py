import os
import sys
import warnings

import numpy as np

if os.name != "nt":
    from fcntl import lockf, LOCK_EX, LOCK_UN
else:
    import msvcrt
# import tempfile

from pysimlink.lib.model_paths import ModelPaths
from pysimlink.utils import annotation_utils as anno
from pysimlink.utils.model_utils import mt_rebuild_check, sanitize_model_name, cast_type
from pysimlink.lib.model_types import DataType, ModelInfo
from pysimlink.lib.spinner import open_spinner
import pickle
import time
import importlib


class Model:
    """
    Instance of the simulink mode. This class compiles and imports
    the model once built. You can have multiple instances of the same
    model in one python runtime.
    """

    _model_paths: "anno.ModelPaths"
    _compiler: "anno.Compiler"

    def __init__(  # pylint: disable=R0913
            self,
            model_name: str,
            path_to_model: str,
            compile_type: str = "grt",
            suffix: str = "rtw",
            tmp_dir: "anno.Optional[str]" = None,
            force_rebuild: bool = False,
            skip_compile: bool = False,
            generator: str = None,
    ):
        """
        Args:
            model_name (str): name of the root simulink model
            path_to_model (str): path to the directory containing code generated from the Simulink Coder *or* the packaged zip file
            compile_type (str): Makefile template used to generate code from Simulink Coder. Only GRT is supported.
            suffix (str): Simulink Coder folders are almost always suffixed with rtw (real time workshop).
            tmp_dir (Optional[str]): Path to the directory that will be used to build the model. Defaults to :file:`__pycache__/{model_name}`
            force_rebuild (bool): force pysimlink to recompile the model from the source located at :code:`path_to_model`. Removes all build artifacts.
            skip_compile (bool): skip compilation of the model. This is useful if you have already compiled the model and just want to import it.
            generator (str): Type of generator to use for cmake. defaults to :code:`NMake Makefiles` on windows and :code:`Unix Makefiles` on mac/linux.


        Attributes:
            orientations: enumeration describing matrix orientations (row major, column major, etc.). This enumeration is
                likely the same among all models, but could change across MATLAB versions.
        """

        self._model_paths = ModelPaths(path_to_model, model_name, compile_type, suffix, tmp_dir, skip_compile)

        if generator is None:
            if os.name == "nt":
                generator = "NMake Makefiles"
            else:
                generator = "Unix Makefiles"

        self._compiler = self._model_paths.compiler_factory(generator)

        self._lock()
        # Check need to compile
        if (
                (mt_rebuild_check(self._model_paths, force_rebuild)
                 or self._compiler.needs_to_compile()) and not skip_compile
        ):
            # Need to compile
            with open_spinner("Compiling"):
                self._compiler.compile()
            with open(os.path.join(self._model_paths.tmp_dir, "compile_info.pkl"), "wb") as f:
                obj = {"pid": os.getpid(), "parent": os.getppid(), "time": time.time()}
                pickle.dump(obj, f)
        self._unlock()

        self.path_dirs = []
        for dir, _, _ in os.walk(
                os.path.join(self._model_paths.tmp_dir, "build", "out", "library")
        ):
            sys.path.append(dir)
            self.path_dirs.append(dir)

        self.module = importlib.import_module(self._model_paths.module_name)
        model_class = getattr(
                self.module, sanitize_model_name(self._model_paths.root_model_name) + "_Model"
        )

        self._model = model_class(self._model_paths.root_model_name)

        self.orientations = getattr(
                self.module,
                sanitize_model_name(self._model_paths.root_model_name) + "_rtwCAPI_Orientation",
        )

    def __del__(self):
        if sys.path is not None and hasattr(self, "path_dirs"):
            for dir in self.path_dirs:
                sys.path.remove(dir)
        # if hasattr(self, "module"):
        # del sys.modules[self.module]
        # sys.modules.remove(self.module)

    def __len__(self):
        """
        Get the total number of steps this model can run
        """
        return int(self.tFinal / self.step_size)

    def _lock(self):
        f = open(os.path.join(self._model_paths.tmp_dir, self._model_paths.root_model_name + ".lock"), "w")
        if os.name == "nt":
            rv = msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        else:
            rv = lockf(f, LOCK_EX)
        f.write(str(os.getpid()))
        f.close()

    def _unlock(self):
        f = open(os.path.join(self._model_paths.tmp_dir, self._model_paths.root_model_name + ".lock"), "w")
        if os.name == "nt":
            rv = msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            rv = lockf(f, LOCK_UN)
        f.close()

    def get_params(self) -> "list[anno.ModelInfo]":
        """
        Return an instance of all parameters, blocks, and signals in the _model

        See :func:`pysimlink.print_all_params` for iterating and printing the contents of this object

        Returns:
            list[:class:`pysimlink.types.ModelInfo`]: List of model info, one for each model (if reference models present). One ModelInfo if no reference models
        """
        return list(map(ModelInfo, self._model.get_params()))

    def reset(self):
        """
        Reset the simulink model. This clears all signal values and reinstantiates the model.
        """
        self._model.reset()

    def step(self, iterations: int = 1):
        """
        Step the simulink model

        Args:
            iterations: Number of timesteps to step internally.
                :code:`model.step(10)` is equivalent to calling :code:`for _ range(10): model.step(1)` functionally, but compiled.

        Raises:
            RuntimeError: If the model encounters an error (these will be raised from simulink). Most commonly, this
                will be `simulation complete`.

        """
        self._model.step(iterations)

    @property
    def tFinal(self) -> float:
        """
        Get the final timestep of the model.

        Returns:
            float: Final timestep of the model (seconds from zero).
        """
        return self._model.tFinal()

    @property
    def step_size(self) -> float:
        """
        Get the step size of the model

        Returns:
            float: step size of the fixed step solver.
        """
        return self._model.step_size()

    def set_tFinal(self, tFinal: float):
        """
        Change the final timestep of the model

        Args:
            tFinal: New final timestep of the model (seconds from zero).

        Raises:
            ValueError: if tFinal is <= 0
        """
        if tFinal <= 0:
            raise ValueError("new tFinal must be > 0")
        self._model.set_tFinal(tFinal)

    def get_signal(self, block_path, model_name=None, sig_name="") -> "np.ndarray":
        """
        Get the value of a signal

        Args:
            block_path: Path to the originating block
            model_name: Name of the model provided by :func:`pysimlink.print_all_params`. None if there are no model
                references (using :code:`None` will retrieve from the root model).
            sig_name: Name of the signal

        Returns:
            Value of the signal at the current timestep
        """
        model_name = self._model_paths.root_model_name if model_name is None else model_name

        sig_type = self._model.desc_signal(model_name, block_path, sig_name)
        if sig_type.cDataType == "struct":
            data = self._model.get_signal_union(model_name, block_path, sig_name)
            return getattr(data, sig_type.mwType)
        else:
            data: "np.ndarray" = self._model.get_signal_arr(model_name, block_path, sig_name)
            if data.size == 1:
                return data.item()
            else:
                return data

    def get_block_param(self, block_path, param, model_name=None) -> "np.ndarray":
        """
        Get the value of a block parameter

        Args:
            block_path: Path the block within the model
            param: Name of the parameter to retrieve
            model_name: Name of the model provided by :func:`pysimlink.print_all_params`. None if there are no model references.

        Returns:
            np.ndarray with the value of the parameter
        """
        model_name = self._model_paths.root_model_name if model_name is None else model_name
        return self._model.get_block_param(model_name, block_path, param)

    def get_model_param(self, param, model_name=None) -> "np.ndarray":
        """
        Get the value of a model parameter

        Args:
            param: Name of the parameter to retrieve
            model_name: Name of the model provided by :func:`pysimlink.print_all_params`. None if there are no model references.

        Returns:
            np.ndarray with the value of the parameter
        """
        model_name = self._model_paths.root_model_name if model_name is None else model_name
        return self._model.get_model_param(model_name, param)

    def get_models(self) -> "list[str]":
        """
        Gets a list of all reference models (and the root model) in this model.

        Returns:
            list of paths, one for each model
        """
        return self._model.get_models()

    def set_block_param(
            self,
            block: str,
            param: str,
            value: "anno.ndarray",
            model_name: "anno.Union[str,None]" = None,
    ):
        """
        Set the parameter of a block within the model.

        Args:
            block: Path to the block within the model
            param: Name of the parameter to change
            value: new value of the parameter
            model_name: Name of the model provided by :func:`pysimlink.print_all_params`. None if there are no model references.
        Raises:
            RuntimeError: If the value array is not the correct shape or orientation as the parameter to change
        """
        model_name = self._model_paths.root_model_name if model_name is None else model_name
        info = self._model.block_param_info(model_name, block, param)
        dtype = DataType(info)

        value = cast_type(value, dtype, self.orientations)

        self._model.set_block_param(model_name, block, param, value)

    def set_model_param(
            self, param: str, value: "anno.ndarray", model_name: "anno.Union[str,None]" = None
    ):
        """
        Set a model parameter.

        Args:
            param: Name of the parameter to change
            value: new value of the parameter
            model_name: Name of the model provided by :func:`pysimlink.print_all_params`. None if there are no model references.
        Raises:
            RuntimeError: If the value array is not the correct shape or orientation as the parameter to change
        """
        model_name = self._model_paths.root_model_name if model_name is None else model_name
        info = self._model.model_param_info(model_name, param)
        dtype = DataType(info)
        value = cast_type(value, dtype, self.orientations)

        self._model.set_model_param(model_name, param, value)
