import argparse

from pysimlink import Model, print_all_params


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_name")
    parser.add_argument("model_path")

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    md = Model(args.model_name, args.model_path)
    md.reset()
    print_all_params(md)


if __name__ == "__main__":
    main()
