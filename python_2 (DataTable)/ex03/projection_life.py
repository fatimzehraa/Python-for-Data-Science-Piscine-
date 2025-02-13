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
        income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_exp = load("life_expectancy_years.csv")
        # print(income)
        # print(life_exp)
        life_exp_1900 = life_exp["1900"]
        income_1900 = income["1900"].apply(convert_to_float)
        dataframes = pd.DataFrame({"income": income_1900, "life_expectancy": life_exp_1900})
        print(dataframes)
        plt.scatter(dataframes["income"], dataframes["life_expectancy"])
        dataframes.set_ylim(300, 10000)
        plt.show()
    except AssertionError as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()