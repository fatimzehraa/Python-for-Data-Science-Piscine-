import sys
import os
import pandas as pd


def load(path: str):
    """function that takes a path as argument,
     writes the dimensions of the data set and returns it."""
    data = pd.read_csv(path, index_col=0)
    print(f"Loading dataset of dimension: {data.shape}")
    return data


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Please provide exactly one argument: \
                the path to the CSV file.")
        elif not os.path.exists(sys.argv[1]):
            raise AssertionError("File does not exist")
        elif not sys.argv[1].endswith('.csv'):
            raise AssertionError("File format not supported")
        print(load(sys.argv[1]))
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
