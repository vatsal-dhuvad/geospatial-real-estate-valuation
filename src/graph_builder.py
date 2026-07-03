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

edges = []

for i in range(len(indices)):
    for j in indices[i]:

        if i != j:

            edges.append((i, j))

print(edges[:10])

print("Edges created successfully.")

from sklearn.decomposition import PCA

features = df.select_dtypes(
    include=["number"]
)

pca = PCA(n_components=2)

embeddings = pca.fit_transform(
    features
)

print(embeddings[:5])

print("Spatial embeddings generated.")

from sklearn.decomposition import PCA

features = df.select_dtypes(
    include=["number"]
)

pca = PCA(n_components=2)

embeddings = pca.fit_transform(
    features
)

print(embeddings[:5])

print("Spatial embeddings generated.")
import matplotlib.pyplot as plt

plt.scatter(
    embeddings[:,0],
    embeddings[:,1]
)

plt.title(
    "Spatial Embeddings"
)

plt.xlabel("Component 1")

plt.ylabel("Component 2")

plt.show()
for i in range(5):

    print(
        "House",
        i,
        "neighbors:",
        indices[i]
    )
