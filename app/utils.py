import pandas as pd

def load_data():
    countries = ["ethiopia", "kenya", "sudan", "tanzania", "nigeria"]
    dfs = []

    for c in countries:
        df = pd.read_csv(f"data/{c}_clean.csv")
        df["Country"] = c.capitalize()
        dfs.append(df)

    return pd.concat(dfs)


def preprocess(df):
    df["DATE"] = pd.to_datetime(df["DATE"])
    return df