# Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load Dataset
master = pd.read_csv("dataset/master_dataset.csv")
print(master.head())

# Features & Target
X = master[
    [
        "Oil_Price",
        "Inflation",
        "GDP_Growth",
        "Forex_Reserves",
        "Trade_Balance"
    ]
]
y = master["USD_INR"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print(X_train.shape)
print(X_test.shape)

# Linear Regression
model = LinearRegression()
model.fit(
    X_train,
    y_train
)
predictions = model.predict(X_test)

# Evaluation Metrics
mae = mean_absolute_error(
    y_test,
    predictions
)
rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)
r2 = r2_score(
    y_test,
    predictions
)
print("\n========== MODEL PERFORMANCE ==========\n")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})
importance["Absolute"] = (
    importance["Coefficient"]
    .abs()
)
importance = (
    importance
    .sort_values(
        "Absolute",
        ascending=False
    )
)
print("\n========== FEATURE IMPORTANCE ==========\n")
print(importance)

#Visualization
plt.figure(figsize=(10,6))
sns.barplot(
    data=importance,
    x="Coefficient",
    y="Feature"
)
plt.title(
    "Feature Importance for USD/INR"
)
plt.xlabel("Coefficient")
plt.ylabel("Economic Indicator")
plt.tight_layout()
plt.savefig(
    "visuals/feature_importance.png",
    dpi=300
)
plt.show()

#Predicted vs Actual
plt.figure(figsize=(8,6))
plt.scatter(
    y_test,
    predictions
)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()]
)
plt.xlabel("Actual USD/INR")
plt.ylabel("Predicted USD/INR")
plt.title(
    "Actual vs Predicted USD/INR"
)
plt.tight_layout()
plt.savefig(
    "visuals/actual_vs_predicted.png",
    dpi=300
)
plt.show()

#Standardized Regression Model
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
importance = pd.DataFrame({
    "Feature": X.columns,
    "Standardized_Coefficient": model.coef_
})
importance["Absolute"] = (
    importance["Standardized_Coefficient"]
    .abs()
)
importance = importance.sort_values(
    "Absolute",
    ascending=False
)
print(importance)

# Multicollinearity Check
vif = pd.DataFrame()
vif["Feature"] = X.columns
vif["VIF"] = [
    variance_inflation_factor(
        X.values,
        i
    )
    for i in range(X.shape[1])
]
print(vif.sort_values(
    "VIF",
    ascending=False
))