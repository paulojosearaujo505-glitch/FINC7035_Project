import pandas as pd
import numpy as np

# 1. Load the clean data from Session 1
print("Loading clean data...")
df = pd.read_csv('output/clean_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)

# 2. Identify the start of the forecast period (2018-2025)
forecast_start = '2018-01-01'
start_idx = df[df['Date'] >= forecast_start].index[0]

results = []

# 3. Loop through each date in the forecast period
print("Calculating Rolling 1-Day 99% VaR and ES...")
for i in range(start_idx, len(df)):
    # Get the previous 500 daily losses (ending at t-1)
    # iloc[i-500:i] gives us exactly 500 rows before the current index i
    past_losses = df['primary_loss'].iloc[i-500:i]
    
    # Sort from largest loss to smallest loss (descending)
    sorted_losses = past_losses.sort_values(ascending=False)
    
    # 99% VaR is the 5th largest loss (index 4 in 0-based indexing)
    var_99 = sorted_losses.iloc[4]
    
    # 99% ES is the average of the 5 largest losses (indices 0 to 4)
    es_99 = sorted_losses.iloc[:5].mean()
    
    # Realized loss for the current day
    realized_loss = df['primary_loss'].iloc[i]
    
    # Check for an exception (realized loss strictly greater than VaR)
    exception = realized_loss > var_99
    
    results.append({
        'Date': df['Date'].iloc[i],
        'Realized_Loss': realized_loss,
        'VaR_99': var_99,
        'ES_99': es_99,
        'Exception': exception
    })

# 4. Save the results to a CSV
results_df = pd.DataFrame(results)
results_df.to_csv('output/var_es_results.csv', index=False)

print("\n--- Calculation Complete ---")
print(f"Results saved to output/var_es_results.csv")
print(f"Total forecast days (2018-2025): {len(results_df)}")
print(f"Total VaR Exceptions: {results_df['Exception'].sum()}")
print(f"Expected Exceptions (1% of forecast days): {len(results_df) * 0.01:.1f}")