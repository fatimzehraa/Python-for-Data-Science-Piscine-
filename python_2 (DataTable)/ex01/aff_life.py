from load_csv import load
import sys
import os
from matplotlib import pyplot as plt

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Please provide exactly one argument: \
                the path to the CSV file.")
        elif not os.path.exists(sys.argv[1]):
            raise AssertionError("File does not exist")
        elif not sys.argv[1].endswith('.csv'):
            raise AssertionError("File format not supported")
        data = load(sys.argv[1])
        morocco = data[data["country"] == "Morocco"]
        # Drop the "country" column and transpose the DataFrame
        c = "country"
        _ylabel = "life_expectancy"
        _title = "Life Expectancy in Morocco"
        morocco = morocco.drop(columns=[c]).set_index(morocco[c].values).T
        morocco.plot(xlabel="year", ylabel=_ylabel, title=_title)
        plt.show()
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
