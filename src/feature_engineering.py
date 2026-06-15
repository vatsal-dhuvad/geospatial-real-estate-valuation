# Feature engineering
import pandas as pd

df = pd.read_csv("data/outlier_removed.csv")

current_year = 2026

df["house_age"] = current_year - df["yr_built"]

df["renovation_age"] = df["yr_renovated"].apply(
    lambda x: 0 if x == 0 else current_year - x
)

print(df[["house_age", "renovation_age"]].head())

df.to_csv("data/feature_engineered.csv", index=False)

print("Feature engineering completed.")