import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except Exception as e:
        print("Error:", e)
        return None