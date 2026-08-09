from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def main():
    df_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")

    if df_income is None or df_life is None:
        return

    x = []
    y = []

    for country in df_life["country"]:
        life_row = df_life[df_life["country"] == country]
        income_row = df_income[df_income["country"] == country]

        if life_row.empty or income_row.empty:
            continue

        life = float(life_row["1900"].iloc[0])
        income = float(income_row["1900"].iloc[0])

        x.append(income)
        y.append(life)

    plt.scatter(x, y)

    plt.title("Life expectancy vs Gross domestic product in 1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()