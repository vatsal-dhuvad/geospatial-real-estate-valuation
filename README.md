# Geospatial Real Estate Valuation using Spatial Embeddings and Graph Neural Networks

## Project Overview

Traditional real estate valuation models primarily rely on tabular features such as the number of bedrooms, bathrooms, and square footage. However, property prices are heavily influenced by spatial factors such as neighboring houses, nearby amenities, and local market conditions.

This project aims to build an advanced geospatial real estate valuation system by incorporating spatial relationships between properties using graph-based machine learning techniques and spatial embeddings.

---

## Objectives

- Build a baseline house price prediction model using XGBoost.
- Capture geographic dependencies between neighboring properties.
- Construct a property graph using K-Nearest Neighbors (KNN).
- Convert spatial relationships into graph structures suitable for Graph Neural Networks (GNNs).
- Prepare the dataset for advanced graph-based learning.

---

## Dataset

**Dataset:** King County Housing Dataset

The dataset contains housing transaction records including:

- Price
- Bedrooms
- Bathrooms
- Square Footage
- Latitude
- Longitude
- Construction Year
- Renovation Year
- Waterfront Information
- Grade and Condition

Dataset Source:
https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

---

## Project Structure

```text
geospatial-real-estate-valuation/
│
├── app/
│
├── data/
│   ├── kc_house_data.csv
│   ├── cleaned_housing.csv
│   ├── outlier_removed.csv
│   └── feature_engineered.csv
│
├── reports/
│   ├── housing_map.html
│   └── houses.geojson
│
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── geospatial_processing.py
│   ├── graph_builder.py
│   ├── map_visualization.py
│   ├── train_xgboost.py
│   └── train_gnn.py
│
├── requirements.txt
├── README.md
└── LICENSE
