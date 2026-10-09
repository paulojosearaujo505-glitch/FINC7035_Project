import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the clean data from Session 1
print("Loading clean data...")
df = pd.read_csv('output/clean_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Calculate the negative daily change in 10Y yield
# We use the basis point change we created in Session 1, but flip the sign.
# This acts as a proxy for the direction of Treasury price changes.
df['neg_delta_10Y_bp'] = -df['delta_10Y_bp']

# 3. Calculate the 252-day rolling correlation
print("Calculating 252-day rolling correlation...")
df['rolling_corr'] = df['SP500_logret'].rolling(window=252, min_periods=252).corr(df['neg_delta_10Y_bp'])

# 4. Drop NaN values (the first 251 days won't have a 252-day window yet)
df_corr = df.dropna(subset=['rolling_corr'])

# 5. Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df_corr['Date'], df_corr['rolling_corr'], color='purple', linewidth=1.5)
plt.axhline(0, color='black', linestyle='--', linewidth=1) # Add a zero line for reference

plt.title('252-Day Rolling Correlation: S&P 500 Returns vs. Negative 10Y Yield Changes', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Correlation', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# 6. Save the figure
plt.savefig('figures/stock_bond_correlation.png', dpi=300)
print("Figure saved to figures/stock_bond_correlation.png")