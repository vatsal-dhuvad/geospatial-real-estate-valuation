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

from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

city_lat = 47.6062
city_lon = -122.3321

df["distance_to_center"] = df.apply(
    lambda row: haversine(
        row["lat"],
        row["long"],
        city_lat,
        city_lon
    ),
    axis=1
)

df.to_csv("data/feature_engineered.csv", index=False)

print("Distance feature added.")