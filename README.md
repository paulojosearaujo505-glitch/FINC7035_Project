# FINC7035: Financial Risk Management - Personal Project

## Project Overview
This repository contains the complete code and data outputs for the FINC7035 Personal Project. The objective of this project was to simulate a real-world risk management scenario by processing raw market data, applying quantitative risk models, and interpreting the results from the perspective of a specific financial institution.

**Institution Selected:** Asset Management Firm  
**Primary Risk Factor:** S&P 500 Equity Market  
**Loss Direction:** `primary_loss = -SP500_logret` (A negative equity return creates a positive loss).

## Project Requirements & Methodology
The project required the analysis of daily market data from 2005 to 2025 (S&P 500 Price Index, 2-Year Treasury Yield, 10-Year Treasury Yield, and US High Yield Spread). The raw data was transformed into risk factors (log returns for equity, first differences in basis points for yields/spreads) to complete the following quantitative tasks:

1. **EWMA Volatility (Task 1):** 
   Calculated the Exponentially Weighted Moving Average (EWMA) volatility using a decay factor of \(\lambda = 0.94\). The recursion was run from the beginning of the dataset, with results displayed for the 2018–2025 period to highlight recent stress episodes.
2. **Stock-Bond Correlation (Task 2):** 
   Calculated a 252-trading-day rolling correlation between S&P 500 daily log returns and the negative daily change in the 10-Year Treasury yield (used as a proxy for Treasury price direction). The full available sample was analyzed to identify correlation regime shifts.
3. **VaR, ES, and Back-Test (Task 3):** 
   Applied a 1-Day 99% Historical Simulation to the daily loss series using a 500-day rolling window. The 99% VaR was defined as the 5th largest loss, and the 99% ES as the average of the 5 largest losses. The model was back-tested over 2018–2025 to identify VaR exceptions.

## Deliverables
The final submission includes a **Risk Analysis Memo (PDF)** (max 6 pages) which interprets the quantitative findings and discusses risk management implications and limitations. The memo focuses on how volatility magnitude/duration, changing diversification benefits, and model lag impact an Asset Management Firm's portfolio.

## Repository Structure
*   `code/`: Contains all Python scripts labeled sequentially to reproduce the figures and risk measures.
    *   `01_data_prep.py`: Cleans raw data, calculates log returns, first differences, and defines the primary loss series.
    *   `02_ewma.py`: Runs the EWMA recursion and plots volatility.
    *   `03_correlation.py`: Calculates the 252-day rolling stock-bond correlation.
    *   `04_var_es.py`: Calculates the 1-day 99% Historical Simulation VaR and ES.
    *   `05_var_es_plot.py`: Plots the VaR/ES back-test and marks exceptions.
*   `data/`: Contains the raw dataset (`Personal_Project_Data.xlsx`).
*   `output/`: Contains the cleaned data (`clean_data.csv`) and VaR/ES results (`var_es_results.csv`).
*   `figures/`: Contains the generated high-resolution plots (`.png`) used in the memo.
*   `draft/`: Contains session notes and the Markdown source (`memo_draft.md`).

## Author
**Paulo Jose Araujo**  
MSc in Finance (2026 Autumn)  
Department of Finance and Business Economics  
Faculty of Business Administration, University of Macau
