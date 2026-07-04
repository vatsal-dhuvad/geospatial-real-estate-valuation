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


from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)
import matplotlib.pyplot as plt

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

results["Error"] = (
    results["Actual"]
    - results["Predicted"]
)

print(
    results.sort_values(
        "Error",
        key=abs,
        ascending=False
    ).head(10)
)

plt.scatter(
    results["Actual"],
    results["Predicted"]
)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")

plt.title("Actual vs Predicted")

plt.show()
import matplotlib.pyplot as plt

importance = model.feature_importances_

feature_names = X.columns

plt.figure(figsize=(10,5))

plt.barh(feature_names[:10], importance[:10])

plt.title("Feature Importance")

plt.show()
