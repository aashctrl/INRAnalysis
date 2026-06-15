#Import
import pandas as pd
import os

# Configuration
INPUT_FOLDER = "dataset/raw"
OUTPUT_FOLDER = "dataset/clean"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Files and their desired column names
datasets = {
    "inflation.csv": "Inflation",
    "gdp_growth.csv": "GDP_Growth",
    "forex_reserves.csv": "Forex_Reserves",
    "exports.csv": "Exports",
    "imports.csv": "Imports",
    "exchange_rate.csv": "USD_INR"
}

for file_name, value_name in datasets.items():
    print(f"Processing {file_name}...")
    file_path = os.path.join(INPUT_FOLDER, file_name)

    # Read World Bank file
    df = pd.read_csv(file_path, skiprows=4)

    # Keep India only
    india = df[df["Country Code"] == "IND"]

    # Extract year columns
    year_cols = [col for col in df.columns if col.isdigit()]

    # Convert wide -> long
    clean_df = (
        india[year_cols]
        .T
        .reset_index()
    )
    clean_df.columns = ["Year", value_name]

    # Convert types
    clean_df["Year"] = clean_df["Year"].astype(int)
    clean_df[value_name] = pd.to_numeric(
        clean_df[value_name],
        errors="coerce"
    )

    # Keep only 1991 onwards
    clean_df = clean_df[
        clean_df["Year"] >= 1991
    ]

    # Save cleaned file
    output_file = os.path.join(
        OUTPUT_FOLDER,
        file_name.replace(".csv", "_clean.csv")
    )

    clean_df.to_csv(output_file, index=False)
    print(f"Saved -> {output_file}")
print("\nAll datasets cleaned successfully.")

oil = pd.read_csv("dataset/raw/oil_price.csv")

# Extract year
oil["Year"] = pd.to_datetime(
    oil["observation_date"],
    dayfirst=True
).dt.year

# Rename column
oil = oil.rename(
    columns={"DCOILBRENTEU": "Oil_Price"}
)

# Keep required columns
oil_clean = oil[["Year", "Oil_Price"]]

# Keep 1991 onwards
oil_clean = oil_clean[oil_clean["Year"] >= 1991]
oil_clean.to_csv(
    "dataset/clean/oil_price_clean.csv",
    index=False
)
print(oil_clean.head())