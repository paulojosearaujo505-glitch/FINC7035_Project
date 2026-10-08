import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the clean data from Session 1
print("Loading clean data...")
df = pd.read_csv('output/clean_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. EWMA Calculation (Recursion from the beginning of the sample)
print("Calculating EWMA Volatility...")
lam = 0.94
variance = np.zeros(len(df))

# Initialize the first variance as the squared first loss (standard approach)
variance[0] = df['primary_loss'].iloc[0]**2

# Apply the EWMA recursion formula
for t in range(1, len(df)):
    # Formula: sigma^2_t = lambda * sigma^2_{t-1} + (1 - lambda) * r^2_{t-1}
    variance[t] = lam * variance[t-1] + (1 - lam) * (df['primary_loss'].iloc[t-1]**2)

# Convert variance to standard deviation (volatility)
df['ewma_vol'] = np.sqrt(variance)

# 3. Filter for the display period (2018-2025)
df_plot = df[df['Date'] >= '2018-01-01'].copy()

# 4. Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df_plot['Date'], df_plot['ewma_vol'], color='darkblue', linewidth=1.5)

plt.title('EWMA Volatility of S&P 500 Daily Losses (λ = 0.94)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('EWMA Volatility (Daily Loss)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# 5. Save the figure
plt.savefig('figures/ewma_volatility.png', dpi=300)
print("Figure saved to figures/ewma_volatility.png")