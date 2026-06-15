# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import os

# Setup
os.makedirs("visuals", exist_ok=True)

# Load Dataset
master = pd.read_csv("dataset/master_dataset.csv")

# Exchange Rate Volatility
master["Exchange_Volatility"] = (
    master["USD_INR"]
    .pct_change()
    .abs()
    * 100
)
master["Exchange_Volatility"] = (
    master["Exchange_Volatility"]
    .fillna(0)
)
master["Yearly_Change"] = (
    master["USD_INR"].pct_change() * 100
)

# Normalization
scaler = MinMaxScaler()
master["Inflation_N"] = scaler.fit_transform(
    master[["Inflation"]]
)
master["GDP_N"] = scaler.fit_transform(
    master[["GDP_Growth"]]
)
master["Forex_N"] = scaler.fit_transform(
    master[["Forex_Reserves"]]
)
master["Trade_N"] = scaler.fit_transform(
    master[["Trade_Balance"]]
)
master["Volatility_N"] = scaler.fit_transform(
    master[["Exchange_Volatility"]]
)

# Reverse Negative Indicators
master["Inflation_N"] = (
    1 - master["Inflation_N"]
)
master["Volatility_N"] = (
    1 - master["Volatility_N"]
)

# Rupee Stability Index
master["RSI"] = (
      master["Forex_N"] * 0.35
    + master["Inflation_N"] * 0.25
    + master["Trade_N"] * 0.20
    + master["GDP_N"] * 0.10
    + master["Volatility_N"] * 0.10
) * 100

# Top Stable Years
ranking = (
    master[
        ["Year", "RSI"]
    ]
    .sort_values(
        "RSI",
        ascending=False
    )
)
print("\n========== TOP 10 MOST STABLE YEARS ==========\n")
print(ranking.head(10))
print("\n========== LEAST STABLE YEARS ==========\n")
print(ranking.tail(10))

# RSI Trend
plt.figure(figsize=(12,6))
plt.plot(
    master["Year"],
    master["RSI"],
    linewidth=2
)
plt.title(
    "Rupee Stability Index (1991-2024)"
)
plt.xlabel("Year")
plt.ylabel("RSI Score")
plt.grid(True)
plt.savefig(
    "visuals/rsi_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Save Results
master.to_csv(
    "dataset/master_dataset_with_rsi.csv",
    index=False
)
ranking.to_csv(
    "visuals/rsi_rankings.csv",
    index=False
)
print(
    "\nRSI analysis completed successfully."
)

