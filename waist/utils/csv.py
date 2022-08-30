import pandas as pd


def reformat(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    df.iloc[:, 2:] = df.iloc[:, 2:] * 25.4

    return df
