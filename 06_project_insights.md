#### **The Indian Rupee Under the Microscope: A Data-Driven Analysis of Currency Movements and Economic Drivers (1991-2024)**



###### **Project Objective**

This project investigates the key macroeconomic factors influencing the Indian Rupee (INR) against the US Dollar (USD) between 1991 and 2024. Using economic indicators such as inflation, GDP growth, foreign exchange reserves, trade balance, and crude oil prices, the study aims to identify the major drivers of currency movements and assess India's economic stability through a custom-built Rupee Stability Index (RSI).



###### **Dataset Summary**

**Metric	Value**

Study Period: 1991-2024

Total Years Analyzed: 34

Variables Used: 8

Source: World Bank, FRED

**Variables:**

* USD/INR Exchange Rate
* Brent Crude Oil Prices
* Inflation Rate
* GDP Growth Rate
* Foreign Exchange Reserves
* Exports
* Imports
* Trade Balance



###### **Key Findings**

**Finding 1: Long-Term Rupee Depreciation**

The Indian Rupee depreciated by approximately 267.9% against the US Dollar between 1991 and 2024.

Strongest INR: 1991 (₹22.74/USD)

Weakest INR: 2024 (₹83+/USD)

This reflects long-term structural changes in India's economy, trade patterns, and global market conditions.

**Finding 2: Economic Variables Explain INR Movements**

A Multiple Linear Regression model achieved:

R² = 0.89

MAE = 3.05

RMSE = 3.24

This indicates that the selected macroeconomic indicators explain approximately 89% of the variation in the USD/INR exchange rate.

**Finding 3: Most Influential Drivers**

Based on standardized coefficients:

**Rank	Variable**

1	Foreign Exchange Reserves

2	Inflation

3	Trade Balance

4	GDP Growth

5	Oil Prices

Foreign Exchange Reserves emerged as the strongest predictor of exchange-rate movements.

**Finding 4: Multicollinearity Exists**

Variance Inflation Factor (VIF) analysis revealed:

**Variable	VIF**

Oil Price	15.51

Trade Balance	10.48

Forex Reserves	5.40

This suggests several macroeconomic variables are highly interrelated and should be interpreted as complementary indicators rather than isolated causal factors.

**Finding 5: Rupee Stability Index (RSI)**

A custom Rupee Stability Index (RSI) was developed using:

Inflation

GDP Growth

Forex Reserves

Trade Balance

Exchange Rate Volatility

The index scores each year on a scale of 0-100.

**Most Stable Years**

**Rank	Year	RSI**

1	2021	81.80

2	2024	78.55

3	2023	78.05

4	2020	74.60

5	2019	71.82

**Least Stable Years**

**Rank	Year	RSI**

1	1998	31.66

2	1992	34.06

3	1991	34.41

4	2012	35.59

5	2009	42.83



###### **Conclusion**

The analysis demonstrates that the Indian Rupee is influenced by a combination of macroeconomic factors rather than a single dominant variable. Foreign exchange reserves, inflation, and trade balance emerged as the strongest predictors of currency movements. Despite periods of economic stress, India's overall currency stability improved substantially over the study period, as reflected by the Rupee Stability Index.

