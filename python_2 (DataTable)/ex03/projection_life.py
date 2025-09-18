from load_csv import load
import pandas as pd
from matplotlib import pyplot as plt


def convert_to_float(data):
    if isinstance(data, str) and 'K' in data:
        data = data.replace("K", "")
        data = float(data) * 1_000
    return data


def main():
    try:
        inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_exp = load("life_expectancy_years.csv")
        x = inc["1900"].apply(convert_to_float)
        y = life_exp["1900"]
        dataframes = pd.DataFrame({"income": x, "life_expectancy": y})
        plt.scatter(dataframes["income"], dataframes["life_expectancy"])
        plt.xscale("log")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.show()
    except AssertionError as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
