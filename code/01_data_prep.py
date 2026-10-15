import pandas as pd
import numpy as np

# 1. Load the data
print("Loading data...")
df = pd.read_excel('data/Personal_Project_Data.xlsx')
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
df = df.sort_values('Date').reset_index(drop=True)

# 2. Transformations
print("Calculating transformations...")
# Equity log return
df['SP500_logret'] = np.log(df['SP500_Price_Index'] / df['SP500_Price_Index'].shift(1))

# First differences (multiplied by 100 to get Basis Points)
df['delta_2Y_bp'] = df['US_Treasury_2Y_Yield'].diff() * 100
df['delta_10Y_bp'] = df['US_Treasury_10Y_Yield'].diff() * 100
df['delta_HY_bp'] = df['US_HighYield_Spread'].diff() * 100

# Asset Management Firm (market drops are adverse)
df['primary_loss'] = -df['SP500_logret']

# 4. Clean up NaNs created by shifting/differencing
df = df.dropna().reset_index(drop=True)

# 5. Save clean dataset
df.to_csv('output/clean_data.csv', index=False)
print("Data transformed and saved to output/clean_data.csv")
print("\n--- First 5 Rows of Clean Data ---")
print(df[['Date', 'primary_loss']].head())