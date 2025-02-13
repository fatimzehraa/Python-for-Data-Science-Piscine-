from load_csv import load
import sys
from matplotlib import pyplot as plt

def main():
    try:
        try:
            path = sys.argv[1]
        except IndexError:
            raise AssertionError("No args") from None
        data = load(path)
        # print(data)
        country = data[(data["country"] == "Morocco") | (data["country"] == "France")]
        print(country)
        country = country.drop(columns=["country"]).set_index(country["country"].values).T
        # print(f"country index: {country.axes}")
        # country.index = country.index.astype(int)
        country = country.apply(lambda col: col.str.replace("M", "").astype(float) * 1_000_000)
        print(f"new table: \n{country}")
        country.plot(xlabel="year", ylabel="population", title="population in Morocco and France")
        plt.show()
    except AssertionError as e:
        print(e)
        exit()
    
if __name__ == "__main__":
    main()