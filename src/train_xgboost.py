# XGBoost model training
import pandas as pd

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

df = pd.read_csv("data/feature_engineered.csv")

X = df.drop(
    columns=[
        "price",
        "date",
        "id"
    ]
)

X = X.select_dtypes(include=["number"])

y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed.")
