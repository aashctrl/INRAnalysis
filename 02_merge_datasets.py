#Import
import pandas as pd

# Load Cleaned Datasets
exchange = pd.read_csv("dataset/clean/exchange_rate_clean.csv")
oil = pd.read_csv("dataset/clean/oil_price_clean.csv")
inflation = pd.read_csv("dataset/clean/inflation_clean.csv")
gdp = pd.read_csv("dataset/clean/gdp_growth_clean.csv")
forex = pd.read_csv("dataset/clean/forex_reserves_clean.csv")
exports = pd.read_csv("dataset/clean/exports_clean.csv")
imports = pd.read_csv("dataset/clean/imports_clean.csv")

# Define Analysis Period
START_YEAR = 1991
END_YEAR = 2024

# Filter Data
exchange = exchange[
    (exchange["Year"] >= START_YEAR) &
    (exchange["Year"] <= END_YEAR)
]
oil = oil[
    (oil["Year"] >= START_YEAR) &
    (oil["Year"] <= END_YEAR)
]
inflation = inflation[
    (inflation["Year"] >= START_YEAR) &
    (inflation["Year"] <= END_YEAR)
]
gdp = gdp[
    (gdp["Year"] >= START_YEAR) &
    (gdp["Year"] <= END_YEAR)
]
forex = forex[
    (forex["Year"] >= START_YEAR) &
    (forex["Year"] <= END_YEAR)
]
exports = exports[
    (exports["Year"] >= START_YEAR) &
    (exports["Year"] <= END_YEAR)
]
imports = imports[
    (imports["Year"] >= START_YEAR) &
    (imports["Year"] <= END_YEAR)
]

# Merge Datasets
master = (
    exchange
    .merge(oil, on="Year", how="inner")
    .merge(inflation, on="Year", how="inner")
    .merge(gdp, on="Year", how="inner")
    .merge(forex, on="Year", how="inner")
    .merge(exports, on="Year", how="inner")
    .merge(imports, on="Year", how="inner")
)

# Create Trade Balance
master["Trade_Balance"] = (
    master["Exports"] -
    master["Imports"]
)

# Sort Data
master = master.sort_values("Year").reset_index(drop=True)

# Data Quality Check
print("\nMissing Values:")
print(master.isnull().sum())
print("\nDataset Shape:")
print(master.shape)
print("\nDataset Info:")
print(master.info())
print("\nPreview:")
print(master.head())
print("\nLast 5 Rows:")
print(master.tail())

# Save Master Dataset
master.to_csv(
    "dataset/master_dataset.csv",
    index=False
)
print("\nmaster_dataset.csv created successfully!")