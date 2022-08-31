import pandas as pd


def reformat(filename: str, in_unit: str = "inch") -> pd.DataFrame:
    df = pd.read_csv(filename)

    if in_unit == "inch":
        df.iloc[:, 2:] = df.iloc[:, 2:] * 2.54
    elif in_unit == "cm":
        df.iloc[:, 2:] = df.iloc[:, 2:] / 2.54

    return df
