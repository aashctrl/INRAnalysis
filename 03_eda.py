#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Save Visuals
os.makedirs("visuals", exist_ok=True)

#Load Dataset
master = pd.read_csv("dataset/master_dataset.csv")

# Data Overview
print("\nDataset Shape:")
print(master.shape)
print("\nColumn Names:")
print(master.columns)
print("\nData Types:")
print(master.dtypes)
print("\nMissing Values:")
print(master.isnull().sum())
print("\nSummary Statistics:")
print(master.describe())

#KPI Metrics
print("\n========== KEY METRICS ==========")
print(
    f"Study Period: "
    f"{master['Year'].min()} - {master['Year'].max()}"
)
print(
    f"Strongest INR: ₹{master['USD_INR'].min():.2f}/USD"
)
print(
    f"Weakest INR: ₹{master['USD_INR'].max():.2f}/USD"
)
print(
    f"Average INR: ₹{master['USD_INR'].mean():.2f}/USD"
)
strongest_year = master.loc[
    master["USD_INR"].idxmin(),
    "Year"
]
weakest_year = master.loc[
    master["USD_INR"].idxmax(),
    "Year"
]
print(
    f"Strongest INR Year: {strongest_year}"
)
print(
    f"Weakest INR Year: {weakest_year}"
)
print(
    f"Total Years Analysed: {len(master)}"
)

#INR Trend Analysis
plt.figure(figsize=(12,6))
plt.plot(
    master["Year"],
    master["USD_INR"],
    linewidth=2
)
plt.title("USD/INR Exchange Rate (1991-2024)")
plt.xlabel("Year")
plt.ylabel("INR per USD")
plt.grid(True)
# Save Plot
plt.savefig(
    "visuals/inr_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

#Oil Price Trend Analysis
plt.figure(figsize=(12,6))
plt.plot(
    master["Year"],
    master["Oil_Price"],
    linewidth=2
)
plt.title("Brent Crude Oil Prices")
plt.xlabel("Year")
plt.ylabel("USD per Barrel")
plt.grid(True)
# Save Plot
plt.savefig(
    "visuals/oil_price_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

#Inflation Trend Analysis
plt.figure(figsize=(12,6))
plt.plot(
    master["Year"],
    master["Inflation"],
    linewidth=2
)
plt.title("Inflation Rate")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")
plt.grid(True)
# Save Plot
plt.savefig(
    "visuals/inflation_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

#INR Depreciation Analysis
start_rate = master["USD_INR"].iloc[0]
end_rate = master["USD_INR"].iloc[-1]
depreciation = (
    (end_rate - start_rate)
    / start_rate
) * 100
print(
    f"INR depreciated by {depreciation:.2f}% "
    f"between 1991 and 2024"
)

# Yearly Depreciation Analysis
master["Yearly_Change"] = (
    master["USD_INR"].pct_change() * 100
)
print("\n========== BIGGEST RUPEE SHOCKS ==========\n")
print(
    master[
        ["Year", "Yearly_Change"]
    ]
    .sort_values(
        "Yearly_Change",
        ascending=False
    )
    .head(10)
)

#Depreciation Trend Chart
plt.figure(figsize=(12,6))
plt.bar(
    master["Year"],
    master["Yearly_Change"]
)
plt.axhline(
    y=0,
    linestyle="--"
)
plt.title("Annual Percentage Change in USD/INR")
plt.xlabel("Year")
plt.ylabel("% Change")
plt.grid(True)
#Save Plot
plt.savefig(
    "visuals/yearly_inr_change.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

#Correlation Analysis
corr = master.corr(numeric_only=True)
plt.figure(figsize=(10,8))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title(
    "Correlation Matrix of Economic Indicators"
)
#Save Plot
plt.savefig(
    "visuals/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
print(corr["USD_INR"].sort_values(ascending=False))

# Correlation Ranking with USD/INR
print("\n========== CORRELATION WITH USD/INR ==========\n")
correlations = (
    master.corr(numeric_only=True)["USD_INR"]
    .sort_values(ascending=False)
)
print(correlations)

# Top Positive and Negative Correlations
print("\n========== TOP DRIVERS ==========\n")
corr_usd = (
    master.corr(numeric_only=True)["USD_INR"]
    .drop("USD_INR")
    .sort_values(ascending=False)
)
print("Strongest Positive Relationships:")
print(corr_usd.head(3))
print("\nStrongest Negative Relationships:")
print(corr_usd.tail(3))

#Scatter Plot Analysis
variables = [
    "Oil_Price",
    "Inflation",
    "Forex_Reserves",
    "Trade_Balance",
    "GDP_Growth"
]
for var in variables:
    plt.figure(figsize=(8, 6))
    sns.regplot(
        x=master[var],
        y=master["USD_INR"],
        scatter_kws={"alpha": 0.7},
        line_kws={"linewidth": 2}
    )
    plt.title(f"{var.replace('_', ' ')} vs USD/INR")
    plt.xlabel(var.replace("_", " "))
    plt.ylabel("USD/INR")
    plt.grid(True)
    # Save Plot
    plt.savefig(
        f"visuals/{var.lower()}_vs_usd_inr.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()

#Rupee Shock Analysis
top_shocks = (
    master[
        ["Year", "Yearly_Change"]
    ]
    .sort_values(
        "Yearly_Change",
        ascending=False
    )
)
top_shocks.to_csv(
    "visuals/rupee_shocks.csv",
    index=False
)

#Key Insights
print("\n========== KEY INSIGHTS ==========\n")
print(
    f"INR depreciated by {depreciation:.2f}% "
    f"between 1991 and 2024."
)
print(
    f"Strongest INR observed in {strongest_year}."
)
print(
    f"Weakest INR observed in {weakest_year}."
)
print(
    f"Highest positive correlation: "
    f"{corr_usd.idxmax()} "
    f"({corr_usd.max():.2f})"
)
print(
    f"Highest negative correlation: "
    f"{corr_usd.idxmin()} "
    f"({corr_usd.min():.2f})"
)