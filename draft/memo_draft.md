University of Macau
Faculty of Business Administration
Department of Finance and Business Economics  


**Course:** FINC7035: Financial Risk Management  
**Instructor:** Jiahong Shi  
**Program:** Master Program (2026 Autumn)  
**Date:** October 30, 2026

---

**MEMORANDUM**

**To:** Chief Risk Officer  
**From:** Paulo Jose Araujo  
**Date:** October 30, 2026  
**Re:** Risk Assessment for Asset Management Firm: S&P 500 Equity Risk (2018–2025)

---

## 1. Introduction and Exposure
*(Summarize Session 1 notes here. Explain your institution and primary risk factor).*
- Institution chosen: Asset Management Firm.
- Primary risk factor: S&P 500 daily log returns.
- Loss direction: `primary_loss = -SP500_logret`. A negative equity return creates a positive loss.
- Why this matters: Asset management firms focus on total return and volatility management. The S&P 500 is the primary driver of portfolio drawdowns and client redemptions. 

## 2. Volatility Risk (EWMA Analysis)
*(Summarize Session 2 notes here. Insert figure placeholder).*
- Look at the EWMA volatility plot. Point out the 2020 spike (magnitude) and the 2022-2023 plateau (duration).
- Why does *duration* matter more for an asset manager than a short spike? (Client attrition, Sharpe ratio drag, expensive rebalancing).
- Mention the 2025 spike as a warning against complacency.
- ![Figure 1: EWMA Volatility of S&P 500 Daily Losses (2018-2025)](../figures/ewma_volatility.png)

## 3. Diversification Risk (Stock-Bond Correlation)
*(Summarize Session 3 notes here. Insert figure placeholder).*
- Explain the pre-2021 negative correlation and why it validated the 60/40 portfolio.
- Explain the 2021-2023 positive correlation spike. What did this mean for the firm? (Stocks and bonds falling together, no safe haven, balanced portfolios suffered severe drawdowns).
- Mention the recent normalization but emphasize the lesson: diversification is not guaranteed.
- ![Figure 2: 252-Day Rolling Correlation: S&P 500 Returns vs. Negative 10Y Yield Changes](../figures/stock_bond_correlation.png)

## 4. Tail Risk and Model Performance (VaR, ES, and Back-Test)
*(Summarize Sessions 4 & 5 notes here. Insert figure placeholder).*
- State the method: 1-day 99% Historical Simulation, 500-day rolling window.
- Report the results: 29 exceptions vs 20.1 expected.
- Discuss the clustering of exceptions (March 2020, 2022, 2025). Why is clustering dangerous for an asset manager? (Model fails exactly when you need it most).
- Discuss the model lag: Historical simulation is reactive, not predictive. 
- Discuss ES vs VaR: ES is always higher, and the gap widens during stress.
- ![Figure 3: 1-Day 99% Historical Simulation VaR, ES, and Back-Test (2018-2025)](../figures/var_es_backtest.png)

## 5. Risk Management Implications and Limitations
- **Main Implication:** The firm cannot rely solely on historical simulation for tail risk. The model lags during regime shifts. The firm should consider using stress testing (e.g., hypothetical scenarios) or combining historical simulation with models that react faster to volatility (like EWMA or GARCH). Also, the breakdown of stock-bond correlation means asset allocation must be dynamic, not static.
- **Important Limitation:** Historical simulation assumes the past 500 days represent the future. It does not adapt quickly to new regimes. Additionally, the stock-bond correlation uses a yield-change proxy, not actual bond returns, which may slightly misrepresent the true diversification benefit.
