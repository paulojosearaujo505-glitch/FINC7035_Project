import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the results from 04_var_es.py
print("Loading VaR/ES results...")
df = pd.read_csv('output/var_es_results.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Create the plot
plt.figure(figsize=(14, 7))

# Plot the realized daily losses (as a thin grey line to see the spikes)
plt.plot(df['Date'], df['Realized_Loss'], color='grey', linewidth=0.8, label='Realized Daily Loss')

# Plot the rolling VaR and ES (as thicker colored lines)
plt.plot(df['Date'], df['VaR_99'], color='blue', linewidth=1.5, label='99% VaR (Historical Simulation)')
plt.plot(df['Date'], df['ES_99'], color='red', linewidth=1.5, linestyle='--', label='99% ES (Historical Simulation)')

# Highlight the exceptions (where Realized Loss > VaR)
exceptions = df[df['Exception'] == True]
plt.scatter(exceptions['Date'], exceptions['Realized_Loss'], 
            color='red', s=40, zorder=5, label='VaR Exceptions')

# Formatting
plt.title('1-Day 99% Historical Simulation VaR, ES, and Back-Test (2018–2025)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Loss (S&P 500)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# 3. Save the figure
plt.savefig('figures/var_es_backtest.png', dpi=300)
print("Figure saved to figures/var_es_backtest.png")