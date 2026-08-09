from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def main():
    df = load("population_total.csv")

    if df is None:
        return

    france = "France"
    angola = "Angola"

    france_data = df[df["country"] == france]
    angola_data = df[df["country"] == angola]


    years = df.columns[1:250].astype(int)
    population_france = france_data.iloc[0, 1:250].str[:-1].astype(float)
    population_angola = angola_data.iloc[0, 1:250].str[:-1].astype(float)

    plt.plot(years, population_france, label="France")
    plt.plot(years, population_angola, label="Angola")

    plt.title(f"Population projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: f"{x:g}M")
    )

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()