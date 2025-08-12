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
        c = "country"
        country = data[(data[c] == "Morocco") | (data[c] == "France")]
        print(country)
        country = country.drop(columns=[c]).set_index(country[c].values).T
        # print(f"country index: {country.axes}")
        # country.index = country.index.astype(int)
        country = country.apply(lambda col: col.str.replace("M", "").astype(float) * 1_000_000)
        print(f"new table: \n{country}")
        _title = "Population in Morocco and France"
        country.plot(xlabel="year", ylabel="population", title=_title)
        plt.show()
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
