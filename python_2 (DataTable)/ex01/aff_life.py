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
        morocco = data[data["country"] == "Morocco"]
        # Drop the "country" column and transpose the DataFrame
        morocco = morocco.drop(columns=["country"]).set_index(morocco["country"].values).T
        morocco.plot(xlabel="year", ylabel="life Expectancy", title="Life Expectancy in Morocco")
        # plt.title("Life Expectancy in Morocco")
        plt.show()
    except AssertionError as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()