//
// Created by landon on 10/24/21.
//
#include "model_utils.hpp"
#include <cstring>
#include <memory>
#include <sstream>
#include <unordered_map>
#include <string>
#include <utility>
#include <tuple>
#include <cassert>

py::buffer_info PYSIMLINK::get_model_param(const rtwCAPI_ModelMappingInfo *mmi, const char *param,
                                  std::unordered_map<map_key_1s, size_t, pair_hash, Compare> &param_map) {
    if (param == nullptr)
        throw std::runtime_error("passed nullptr to get_model_param as search param");

    const rtwCAPI_ModelParameters *capiModelParams = rtwCAPI_GetModelParameters(mmi);


    int param_index = -1;
    std::unordered_map<map_key_1s, size_t, pair_hash, Compare>::const_iterator it;
    map_key_1s key{std::string(param), mmi};
    it = param_map.find(key);
    if (it == param_map.end()) {
        uint_T nParams = rtwCAPI_GetNumModelParameters(mmi);
        for (size_t i = 0; i < nParams; i++) {
            if (strcmp(capiModelParams[i].varName, param) == 0) {
                // correct param
                param_index = i;
                //std::string tmp = param;
                param_map[key] = i;
                break;
            }
        }
    } else {
        param_index = it->second;
    }

    if (param_index == -1) {
        // never found the parameter
        std::stringstream err("");
        err << "get_model_param: Parameter (" << param << ") does not exist in model";
        throw std::runtime_error(err.str().c_str());
    }

    rtwCAPI_DataTypeMap dt = mmi->staticMap->Maps.dataTypeMap[rtwCAPI_GetModelParameterDataTypeIdx(capiModelParams,
                                                                                                   param_index)];
    void *addr = mmi->InstanceMap.dataAddrMap[rtwCAPI_GetModelParameterAddrIdx(capiModelParams, param_index)];
    rtwCAPI_DimensionMap paramDim = rtwCAPI_GetDimensionMap(mmi)[rtwCAPI_GetBlockParameterDimensionIdx(
            capiModelParams, param_index)];
    return PYSIMLINK::from_buffer_struct(PYSIMLINK::format_pybuffer(mmi, dt, paramDim, addr));
}

py::buffer_info PYSIMLINK::get_block_param(const rtwCAPI_ModelMappingInfo *mmi, const char *block, const char *param,
                                           std::unordered_map<map_key_2s, size_t, pair_hash, Compare> &param_map) {
    std::unordered_map<map_key_2s, size_t, pair_hash, Compare>::const_iterator it;
    int param_iter = -1;

    const rtwCAPI_BlockParameters *capiBlockParameters = rtwCAPI_GetBlockParameters(mmi);
    uint_T nParams = rtwCAPI_GetNumBlockParameters(mmi);
    std::string first(block == nullptr ? "" : block);
    std::string second(param == nullptr ? "" : param);
    map_key_2s key{first, second, mmi};
    it = param_map.find(key);
    if (it == param_map.end()) {
        for (size_t i = 0; i < nParams; i++) {
            if (strcmp(block, capiBlockParameters[i].blockPath) == 0 &&
                strcmp(param, capiBlockParameters[i].paramName) == 0) {
                // correct param
                param_map[key] = i;
                param_iter = i;
                break;
            }
        }
    } else {
        param_iter = it->second;
    }

    if (param_iter == -1) {
        std::stringstream err("");
        err << "get_block_param: Parameter (" << block << ',' << param << ") does not exist in model";
        throw std::runtime_error(err.str().c_str());
    }

    rtwCAPI_DataTypeMap dt = mmi->staticMap->Maps.dataTypeMap[rtwCAPI_GetBlockParameterDataTypeIdx(capiBlockParameters,
                                                                                                   param_iter)];
    rtwCAPI_DimensionMap sigDim = rtwCAPI_GetDimensionMap(mmi)[rtwCAPI_GetBlockParameterDimensionIdx(
            capiBlockParameters, param_iter)];
    void *addr = mmi->InstanceMap.dataAddrMap[rtwCAPI_GetBlockParameterAddrIdx(capiBlockParameters, param_iter)];
    return PYSIMLINK::from_buffer_struct(PYSIMLINK::format_pybuffer(mmi, dt, sigDim, addr));
}

struct std::unique_ptr<PYSIMLINK::signal_info> PYSIMLINK::get_signal_val(const rtwCAPI_ModelMappingInfo *mmi,
                                          std::unordered_map<map_key_2s, size_t, pair_hash, Compare> &sig_map,
                                          const char *block, const char *sigName) {


    assert(mmi != nullptr);
    std::unordered_map<map_key_2s, size_t, pair_hash, Compare>::const_iterator it;

    if (block == nullptr && sigName == nullptr)
        throw std::runtime_error("get_signal_val: Must specify signal name or origin block to search for signal");

    uint_T numSigs = rtwCAPI_GetNumSignals(mmi);
    const rtwCAPI_Signals *capiSignals = rtwCAPI_GetSignals(mmi);

    int param_index = -1;

    std::string first(block == nullptr ? "" : block);
    std::string second(sigName == nullptr ? "" : sigName);
    map_key_2s key{first, second, mmi};
    it = sig_map.find(key);
    if (it == sig_map.end()) {

        for (size_t i = 0; i < numSigs; i++) {
            if ((sigName == nullptr && strcmp(block, rtwCAPI_GetSignalBlockPath(capiSignals, i)) == 0) ||
                (block == nullptr && strcmp(sigName, rtwCAPI_GetSignalName(capiSignals, i)) == 0) ||
                ((sigName != nullptr && block != nullptr) &&
                 (strcmp(rtwCAPI_GetSignalName(capiSignals, i), sigName) == 0 && strcmp(
                         rtwCAPI_GetSignalBlockPath(capiSignals, i), block) == 0))) {
                // signal match
                sig_map[key] = i;
                param_index = i;
                break;
            }
        }
    } else {
        param_index = it->second;
    }

    if (param_index == -1) {
        std::stringstream err("");
        err << "get_signal_val: Parameter (" << block << ',' << (sigName == nullptr ? "" : sigName)
            << ") does not exist in provided model";
        throw std::runtime_error(err.str().c_str());
    }


    rtwCAPI_DataTypeMap dt = rtwCAPI_GetDataTypeMap(mmi)[rtwCAPI_GetSignalDataTypeIdx(capiSignals, param_index)];
    rtwCAPI_DimensionMap sigDim = rtwCAPI_GetDimensionMap(mmi)[rtwCAPI_GetSignalDimensionIdx(capiSignals, param_index)];
    void *addr = rtwCAPI_GetDataAddressMap(mmi)[rtwCAPI_GetSignalAddrIdx(capiSignals, param_index)];

    // use malloc instead of new so we don't call every constructor. This looks nasty because we also have to use free
    std::unique_ptr<PYSIMLINK::signal_info> ret(new PYSIMLINK::signal_info);
    if(strcmp(dt.cDataName, "void") == 0 || strcmp(dt.cDataName, "struct") == 0){
        ret->is_array = false;
        ret->type_size = dt.dataSize;
        strcpy(ret->struct_name, dt.mwDataName);
        ret->data.addr = addr;
    }else{
        ret->is_array = true;
        PYSIMLINK::format_pybuffer(mmi, dt, sigDim, addr, &ret->data.arr);
    }
    return ret;
}


void PYSIMLINK::format_pybuffer(const rtwCAPI_ModelMappingInfo *mmi, rtwCAPI_DataTypeMap dt, rtwCAPI_DimensionMap sigDim,
                           void *addr, PYSIMLINK::BufferLike *ret) {

    // doesn't matter where the buffer is (stack or heap), fill them the same
    // this way we don't have to copy vectors from stack->heap when it's assigned to the heap
    ret->ptr = addr;
    ret->itemsize = dt.dataSize;

    if (strcmp(dt.cDataName, "int") == 0) {
        strcpy(ret->format, py::format_descriptor<int>::format().c_str());
    } else if (strcmp(dt.cDataName, "float") == 0) {
        strcpy(ret->format, py::format_descriptor<float>::format().c_str());
    } else if (strcmp(dt.cDataName, "double") == 0) {
        strcpy(ret->format, py::format_descriptor<double>::format().c_str());
    } else if (strcmp(dt.cDataName, "char") == 0) {
        strcpy(ret->format, py::format_descriptor<char>::format().c_str());
    } else if (strcmp(dt.cDataName, "unsigned char") == 0) {
        strcpy(ret->format, py::format_descriptor<unsigned char>::format().c_str());
    } else if (strcmp(dt.cDataName, "short") == 0) {
        strcpy(ret->format, py::format_descriptor<short>::format().c_str());
    } else if (strcmp(dt.cDataName, "unsigned short") == 0) {
        strcpy(ret->format, py::format_descriptor<unsigned short>::format().c_str());
    } else if (strcmp(dt.cDataName, "long") == 0) {
        strcpy(ret->format, py::format_descriptor<long>::format().c_str());
    } else if (strcmp(dt.cDataName, "unsigned int") == 0) {
        strcpy(ret->format, py::format_descriptor<unsigned int>::format().c_str());
    } else if (strcmp(dt.cDataName, "unsigned long") == 0) {
        strcpy(ret->format, py::format_descriptor<unsigned long>::format().c_str());
    } else {
        std::stringstream err("");
        err << "Parameter has invalid cDataName(" << dt.cDataName << ") (internal error)";
        throw std::runtime_error(err.str().c_str());
    }
    ret->ndim = sigDim.numDims;
    if (ret->ndim > 3) {
        throw std::runtime_error(
                "Cannot return values with more than 3 dimensions...yet. Fix the issue and open a pull request!");
    }
    for (size_t i = 0; i < ret->ndim; i++) {
        ssize_t dim_size = rtwCAPI_GetDimensionArray(mmi)[sigDim.dimArrayIndex + i];
        ssize_t cur_stride;
        ret->shape[i] = dim_size;
        switch (sigDim.orientation) {
            case rtwCAPI_Orientation::rtwCAPI_SCALAR:
            case rtwCAPI_Orientation::rtwCAPI_VECTOR:
                ret->strides[i] = dt.dataSize;
                break;
            case rtwCAPI_Orientation::rtwCAPI_MATRIX_COL_MAJOR:
            case rtwCAPI_Orientation::rtwCAPI_MATRIX_COL_MAJOR_ND:
                cur_stride = dt.dataSize;
                for(size_t j = 0; j < i; j++){
                    cur_stride *= rtwCAPI_GetDimensionArray(mmi)[sigDim.dimArrayIndex + j];
                }
                ret->strides[i] = cur_stride;
                break;
            case rtwCAPI_Orientation::rtwCAPI_MATRIX_ROW_MAJOR:
                if (i == 0)
                    ret->strides[i] = dt.dataSize * dim_size;
                else
                    ret->strides[i] = dt.dataSize;
                break;
            case rtwCAPI_Orientation::rtwCAPI_MATRIX_ROW_MAJOR_ND:
                throw std::runtime_error(
                        "ND matrices not supported in row major orientation. Use column major for 3-dim matrices");
                break;
            default:
                throw std::runtime_error("Invalid/Unknown orientation for parameter (internal error)");
        }
    }

    ret->readonly = true;
}

PYSIMLINK::BufferLike
PYSIMLINK::format_pybuffer(const rtwCAPI_ModelMappingInfo *mmi, rtwCAPI_DataTypeMap dt, rtwCAPI_DimensionMap sigDim,
                           void *addr) {
    // allocate the buffer on the stack, proceed like normal
    PYSIMLINK::BufferLike ret;
    format_pybuffer(mmi, dt, sigDim, addr, &ret);
    return ret;
}

void PYSIMLINK::set_block_param(const rtwCAPI_ModelMappingInfo *mmi, const char *block, const char *param, py::array value) {
    // TODO: cache the param index here
    const rtwCAPI_BlockParameters *capiBlockParameters = rtwCAPI_GetBlockParameters(mmi);
    uint_T nParams = rtwCAPI_GetNumBlockParameters(mmi);
    for (size_t i = 0; i < nParams; i++) {
        if (strcmp(block, capiBlockParameters[i].blockPath) == 0 &&
            strcmp(param, capiBlockParameters[i].paramName) == 0) {
//            validate_scalar(mmi, capiBlockParameters[i], "set_block_parameter", block);

            rtwCAPI_DataTypeMap dt = rtwCAPI_GetDataTypeMap(mmi)[rtwCAPI_GetBlockParameterDataTypeIdx(
                    capiBlockParameters, i)];
            rtwCAPI_DimensionMap blockDim = rtwCAPI_GetDimensionMap(mmi)[rtwCAPI_GetBlockParameterDimensionIdx(
                    capiBlockParameters, i)];
            void *addr = rtwCAPI_GetDataAddressMap(mmi)[rtwCAPI_GetBlockParameterAddrIdx(capiBlockParameters, i)];

            PYSIMLINK::fill_from_buffer(mmi, dt, blockDim, addr, value);
            return;
        }
    }
    std::stringstream err("");
    err << "set_block_param: Parameter (" << block << ',' << param << ") does not exist in model";
    throw std::runtime_error(err.str().c_str());

}

std::vector<struct PYSIMLINK::ModelParam> PYSIMLINK::debug_model_params(const rtwCAPI_ModelMappingInfo *mmi) {
    uint_T numParams = rtwCAPI_GetNumModelParameters(mmi);
    const rtwCAPI_ModelParameters *capiModelParams = rtwCAPI_GetModelParameters(mmi);
    std::vector<struct PYSIMLINK::ModelParam> ret;
    ret.reserve(numParams);
    for (size_t i = 0; i < numParams; i++) {
        struct PYSIMLINK::ModelParam to_add;
        to_add.model_param = capiModelParams[i].varName;
        to_add.data_type = PYSIMLINK::populate_dtype(mmi, capiModelParams[i]);
        ret.push_back(to_add);
    }
    return ret;
}

std::vector<struct PYSIMLINK::BlockParam> PYSIMLINK::debug_block_param(const rtwCAPI_ModelMappingInfo *mmi) {
    const rtwCAPI_BlockParameters *capiBlockParams = rtwCAPI_GetBlockParameters(mmi);
    uint_T nParams = rtwCAPI_GetNumBlockParameters(mmi);
    std::vector<struct PYSIMLINK::BlockParam> ret;
    ret.reserve(nParams);

    for (size_t i = 0; i < nParams; i++) {
        struct PYSIMLINK::BlockParam to_add;
        to_add.block_name = capiBlockParams[i].blockPath;
        to_add.block_param = capiBlockParams[i].paramName;
        to_add.data_type = PYSIMLINK::populate_dtype(mmi, capiBlockParams[i]);
        ret.push_back(to_add);
    }
    return ret;
}

std::vector<struct PYSIMLINK::Signal> PYSIMLINK::debug_signals(const rtwCAPI_ModelMappingInfo *mmi) {
    uint_T numSigs = rtwCAPI_GetNumSignals(mmi);
    const rtwCAPI_Signals *capiSignals = rtwCAPI_GetSignals(mmi);

    std::vector<struct PYSIMLINK::Signal> ret;
    ret.reserve(numSigs);
    for (size_t i = 0; i < numSigs; i++) {
        struct PYSIMLINK::Signal to_add;
        to_add.block_name = PYSIMLINK::safe_string(capiSignals[i].blockPath);
        to_add.signal_name = PYSIMLINK::safe_string(capiSignals[i].signalName);
        to_add.data_type = PYSIMLINK::populate_dtype(mmi, capiSignals[i]);
        ret.push_back(to_add);
    }
    return ret;
}

PYSIMLINK::ModelInfo PYSIMLINK::debug_model_info(const rtwCAPI_ModelMappingInfo *mmi) {
    struct PYSIMLINK::ModelInfo ret;
    ret.model_name = mmi->InstanceMap.path == nullptr ? "root" : std::string(mmi->InstanceMap.path);
    ret.block_params = debug_block_param(mmi);
    ret.model_params = debug_model_params(mmi);
    ret.signals = debug_signals(mmi);

    return ret;
}

void
PYSIMLINK::fill_from_buffer(const rtwCAPI_ModelMappingInfo *mmi, rtwCAPI_DataTypeMap dt, rtwCAPI_DimensionMap blockDim,
                            void *addr, py::array value) {
    // data type check
    std::string dtype_raw = repr(PYBIND11_STR_TYPE(value.dtype()));
    auto cit = PYSIMLINK::c_python_dtypes.find(dt.cDataName);
    if (cit == PYSIMLINK::c_python_dtypes.end()) {
        std::stringstream ss;
        ss << "Unknown C datatype. Not present in datatype map. ";
        ss << "Got " << dt.cDataName;
        throw std::runtime_error(ss.str());
    }

    if (strncmp(cit->second.c_str(), dtype_raw.c_str(), strlen(cit->second.c_str())) == 0 ||
        dt.dataSize != value.itemsize()) {
        std::stringstream ss;
        ss << "Datatype of array does not match datatype of Parameter. ";
        ss << "Expected " << cit->second.c_str() << " got dtype " << dtype_raw.c_str();
        throw std::runtime_error(ss.str());
    }

    // dimension check
    if (blockDim.numDims != value.ndim()) {
        std::stringstream ss;
        ss << "Dimension mismatch. ";
        ss << "Expected " << (int)blockDim.numDims << " got " << value.ndim();
        throw std::runtime_error(ss.str());
    }

    switch (blockDim.orientation) {
        case rtwCAPI_MATRIX_COL_MAJOR_ND:
            if (blockDim.numDims > 3)
                throw std::runtime_error(
                        "Cannot change parameters with more than 3 dimensions...yet. Open a pull request!");
            break;
        case rtwCAPI_MATRIX_ROW_MAJOR_ND:
            throw std::runtime_error("Row major orientation for nd matrices not supported...yet.");
            break;
        default:
            break;
    }

    // perform the actual copy
    memcpy(addr, value.data(), value.nbytes());
}

std::string PYSIMLINK::translate_c_type_name(const std::string& c_name, bool should_throw) {
    auto finder = PYSIMLINK::c_python_dtypes.find(c_name);
    if(finder == PYSIMLINK::c_python_dtypes.end()){
        if(should_throw){
            std::stringstream ss;
            ss << "could not find matching python dtype for " << c_name;
            throw std::runtime_error(ss.str());
        }else{
            return "void";
        }
    }else{
        return finder->second;
    }
}

struct PYSIMLINK::DataType PYSIMLINK::describe_block_param(const rtwCAPI_ModelMappingInfo *mmi, const char *block_path,
                                                           const char *param) {
    const rtwCAPI_BlockParameters *capiBlockParameters = rtwCAPI_GetBlockParameters(mmi);
    uint_T nParams = rtwCAPI_GetNumBlockParameters(mmi);
    for (size_t i = 0; i < nParams; i++) {
        if (strcmp(block_path, capiBlockParameters[i].blockPath) == 0 &&
            strcmp(param, capiBlockParameters[i].paramName) == 0) {
            return PYSIMLINK::populate_dtype(mmi, capiBlockParameters[i]);
        }
    }
}

void PYSIMLINK::set_model_param(const rtwCAPI_ModelMappingInfo *mmi, const char *param, py::array value) {
    // TODO: cache the param index here
    const rtwCAPI_ModelParameters *capiModelParameters = rtwCAPI_GetModelParameters(mmi);
    uint_T nParams = rtwCAPI_GetNumModelParameters(mmi);
    for (size_t i = 0; i < nParams; i++) {
        if (strcmp(param, capiModelParameters[i].varName) == 0) {
//            validate_scalar(mmi, capiModelParameters[i], "set_block_parameter", block);

            rtwCAPI_DataTypeMap dt = rtwCAPI_GetDataTypeMap(mmi)[rtwCAPI_GetModelParameterDataTypeIdx(
                    capiModelParameters, i)];
            rtwCAPI_DimensionMap blockDim = rtwCAPI_GetDimensionMap(mmi)[rtwCAPI_GetModelParameterDimensionIdx(
                    capiModelParameters, i)];
            void *addr = rtwCAPI_GetDataAddressMap(mmi)[rtwCAPI_GetModelParameterAddrIdx(capiModelParameters, i)];

            PYSIMLINK::fill_from_buffer(mmi, dt, blockDim, addr, value);
            return;
        }
    }
    std::stringstream err("");
    err << "set_model_param: Parameter (" << param << ") does not exist in model";
    throw std::runtime_error(err.str().c_str());
}

struct PYSIMLINK::DataType PYSIMLINK::describe_model_param(const rtwCAPI_ModelMappingInfo *mmi, const char *param) {
    const rtwCAPI_ModelParameters *capiModelParameters = rtwCAPI_GetModelParameters(mmi);
    uint_T nParams = rtwCAPI_GetNumModelParameters(mmi);
    for (size_t i = 0; i < nParams; i++) {
        if (strcmp(param, capiModelParameters[i].varName) == 0) {
            return PYSIMLINK::populate_dtype(mmi, capiModelParameters[i]);
        }
    }
}

struct PYSIMLINK::DataType PYSIMLINK::describe_signal(const rtwCAPI_ModelMappingInfo *mmi, const char* block, const char* sigName, std::unordered_map<map_key_2s, size_t, pair_hash, Compare> &sig_map){
    assert(mmi != nullptr);
    std::unordered_map<map_key_2s, size_t, pair_hash, Compare>::const_iterator it;

    if (block == nullptr && sigName == nullptr)
        throw std::runtime_error("get_signal_val: Must specify signal name or origin block to search for signal");

    uint_T numSigs = rtwCAPI_GetNumSignals(mmi);
    const rtwCAPI_Signals *capiSignals = rtwCAPI_GetSignals(mmi);

    int param_index = -1;

    std::string first(block == nullptr ? "" : block);
    std::string second(sigName == nullptr ? "" : sigName);
    map_key_2s key{first, second, mmi};
    it = sig_map.find(key);
    if (it == sig_map.end()) {

        for (size_t i = 0; i < numSigs; i++) {
            if ((sigName == nullptr && strcmp(block, rtwCAPI_GetSignalBlockPath(capiSignals, i)) == 0) ||
                (block == nullptr && strcmp(sigName, rtwCAPI_GetSignalName(capiSignals, i)) == 0) ||
                ((sigName != nullptr && block != nullptr) &&
                 (strcmp(rtwCAPI_GetSignalName(capiSignals, i), sigName) == 0 && strcmp(
                         rtwCAPI_GetSignalBlockPath(capiSignals, i), block) == 0))) {
                // signal match
                sig_map[key] = i;
                param_index = i;
                break;
            }
        }
    } else {
        param_index = it->second;
    }

    if (param_index == -1) {
        std::stringstream err("");
        err << "get_signal_val: Parameter (" << block << ',' << (sigName == nullptr ? "" : sigName)
            << ") does not exist in provided model";
        throw std::runtime_error(err.str().c_str());
    }

    return PYSIMLINK::populate_dtype(mmi, capiSignals[param_index]);
//
//    rtwCAPI_DataTypeMap dt = rtwCAPI_GetDataTypeMap(mmi)[rtwCAPI_GetSignalDataTypeIdx(capiSignals, param_index)];
//    rtwCAPI_DimensionMap sigDim = rtwCAPI_GetDimensionMap(mmi)[rtwCAPI_GetSignalDimensionIdx(capiSignals, param_index)];
//    PYSIMLINK::DataType ret = {
//            .cDataType = dt.cDataName,
//            .orientation = sigDim.orientation,
//            .dims = sigDim.numDims,
//            .pythonType = dt.
//    };
}

py::buffer_info PYSIMLINK::from_buffer_struct(const PYSIMLINK::BufferLike &buffer){
    py::buffer_info ret;

    ret.ptr = buffer.ptr;
    ret.itemsize = buffer.itemsize;
    ret.format = buffer.format;
    ret.ndim = buffer.ndim;
    for(size_t i=0; i < ret.ndim; i++){
        ret.shape.push_back(buffer.shape[i]);
        ret.strides.push_back(buffer.strides[i]);
    }
    ret.readonly = buffer.readonly;

    return ret;
}
