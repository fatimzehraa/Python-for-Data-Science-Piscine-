import pandas as pd


def load(path: str):
    """function that takes a path as argument,
     writes the dimensions of the data set and returns it."""
    data = pd.read_csv(path)
    print(f"Loading dataset of dimension: {data.shape}")
    return data
