from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")

    if df is None:
        return

    country = "France"

    country_data = df[df["country"] == country]

    years = df.columns[1:].astype(int)
    life_expectancy = country_data.iloc[0, 1:].astype(float)

    plt.plot(years, life_expectancy)

    plt.title(f"Life expectancy in {country}")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    plt.show()


if __name__ == "__main__":
    main()