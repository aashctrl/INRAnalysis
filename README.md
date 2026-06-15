The Indian Rupee Under the Microscope
A Data-Driven Analysis of Currency Movements and Economic Drivers (1991–2024)

Project Overview
The Indian Rupee has undergone significant changes since India's economic liberalization in 1991. 
This project investigates the key macroeconomic factors influencing the USD/INR exchange rate and evaluates India's currency stability using a custom-built Rupee Stability Index (RSI).
Using economic data from 1991 to 2024, this analysis explores the relationship between exchange rates, inflation, GDP growth, foreign exchange reserves, trade balance, and crude oil prices.

Objectives
Analyze long-term USD/INR exchange rate trends
Identify macroeconomic drivers of currency movements
Measure the impact of inflation, GDP growth, forex reserves, trade balance, and oil prices
Build a predictive regression model for USD/INR
Develop a custom Rupee Stability Index (RSI)
Create an interactive Power BI dashboard for visualization and insights

Dataset Sources
USD/INR Exchange Rate: World Bank
Inflation Rate: World Bank
GDP Growth Rate: World Bank
Foreign Exchange Reserves: World Bank
Exports & Imports: World Bank
Brent Crude Oil Prices: FRED (Federal Reserve Economic Data)
Study Period: 1991–2024

Tech Stack
Data Analysis: Python,Pandas,NumPy
Visualization: Matplotlib,Seaborn,Power BI
Machine Learning: Scikit-Learn,Linear Regression

Project Structure
INRAnalysis/
│
├── dataset/
│   ├── exchange_rate.csv
│   ├── inflation.csv
│   ├── gdp_growth.csv
│   ├── forex_reserves.csv
│   ├── export.csv
│   ├── import.csv
│   ├── oil_price.csv
│   └── master_dataset_with_rsi.csv
│
├── visuals/
│
├── 01_clean_data.py
├── 02_merge_datasets.py
├── 03_eda.py
├── 04_feature_analysis.py
├── 05_rupee_stability_index.py
├── 06_project_insights.md
│
├── INR_Dashboard.pbix
└── README.md

Methodology
Phase 1: Data Collection & Cleaning
Collected macroeconomic indicators from World Bank and FRED
Cleaned and standardized yearly data
Merged multiple datasets into a unified analytical dataset
Phase 2: Exploratory Data Analysis
Exchange rate trend analysis
Inflation trend analysis
Oil price analysis
Correlation analysis
Phase 3: Feature Analysis
Multiple Linear Regression
Feature Importance Analysis
Multicollinearity Detection using VIF
Phase 4: Rupee Stability Index (RSI)
A custom stability score was created using:
Inflation
GDP Growth
Forex Reserves
Trade Balance
Exchange Rate Volatility
The index scores each year on a scale of 0–100.

Key Findings
INR Depreciation
The Indian Rupee depreciated by: 267.9% between 1991 and 2024.
Regression Performance
Metric	Value
R² Score: 0.89
MAE: 3.05
RMSE: 3.24
The selected economic indicators explain approximately 89% of the variation in the USD/INR exchange rate.
Most Influential Economic Drivers
Rank	Indicator
1	Foreign Exchange Reserves
2	Inflation
3	Trade Balance
4	GDP Growth
5	Oil Prices
Most Stable Years
Year	RSI
2021	81.80
2024	78.55
2023	78.05
2020	74.60
2019	71.82
Least Stable Years
Year	RSI
1998	31.66
1992	34.06
1991	34.41
2012	35.59
2009	42.83

Power BI Dashboard
The interactive dashboard includes:

USD/INR Trend Analysis
Rupee Stability Index Trend
Annual INR Change Analysis
Feature Importance Visualization
Forex Reserves vs Exchange Rate Analysis
Stability Rankings
Dynamic Filters & Slicers

Business Insights
Foreign exchange reserves emerged as the strongest driver of INR stability.
Inflation showed a significant negative relationship with currency strength.
India's currency stability improved substantially after 2014.
The post-2019 period recorded the highest stability scores in the study.
Economic indicators collectively explain most long-term exchange-rate movements.

Future Enhancements
Time Series Forecasting (ARIMA/Prophet)
Exchange Rate Prediction Dashboard
Global Currency Comparison Module
Real-Time Economic Data Integration
👤 Author

Aashi Agrawal

Aspiring Data Analyst | Python | SQL | Power BI | Business Analytics
