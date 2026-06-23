# Graph construction logic
import pandas as pd
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("data/feature_engineered.csv")

coords = df[["lat", "long"]]

knn = NearestNeighbors(n_neighbors=5)

knn.fit(coords)

distances, indices = knn.kneighbors(coords)

print(indices[:5])

print("KNN graph constructed successfully.")