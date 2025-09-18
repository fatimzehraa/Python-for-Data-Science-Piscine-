# import sys
# import pandas as pd

# def load(path: str):
#     """function that takes a path as argument, writes the dimensions of the data set
# and returns it."""
#     try:
#         if not path:
#             raise AssertionError("No file path provided")
#         if not path.lower().endswith('.csv'):
#             raise AssertionError("File format not supported")
#         data = pd.read_csv(path)
#         print(f"Loading dataset of dimension: {data.shape}")
#         return data
#     except FileNotFoundError:
#         raise AssertionError("File not found", path) from None
#     except AssertionError as e:
#         print(e)
#         exit()
        
# print(load(sys.argv[1]))

import pandas as pd


def load(path: str):
    """function that takes a path as argument,
     writes the dimensions of the data set and returns it."""
    data = pd.read_csv(path)
    # print(f"Loading dataset of dimension: {data.shape}")
    return data
