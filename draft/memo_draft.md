# Risk Assessment for Asset Management Firm: S&P 500 Equity Risk (2018–2025)

**Paulo Jose Araujo**

Department of Finance and Business Economics  
Faculty of Business Administration  
University of Macau 


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
This memo presents a quantitative risk assessment for an Asset Management Firm managing diversified investment portfolios. The firm’s core objective is to generate total return for clients while managing volatility and protecting capital against severe drawdowns. Because equity exposure is the primary driver of portfolio performance and the main source of downside risk, the chosen primary risk factor for this analysis is the daily log return of S&P500 Price Index. 

To model risk accurately from the perspective of a long-only equity exposure, I define a daily loss series where a larger positive value represents a worse outcome. The daily loss is calculated as the negative daily log return on the S&P 500 (‘primary_loss = -SP500_logret’). By flipping the sign, a 2% drop in the equity market is recorded as a positive 2% loss. This transformation allows me to apply standard tail-risk model such as Value at Risk (VaR) and Expected Shortfall (ES) to measure the severity of potential drawdowns. 

Understanding this exposure is critical for the firm. Severe equity market downturns directly weaken client capital, which can trigger mass redemptions, damage the firm’s reputation, and reduce assets under management (AUM). The following sections analyze this risk through three distinct lenses: recent volatility dynamics, the changing correlation between stocks and government bonds, and the performance of my tail-risk models during recent market crises. 



## 2. Volatility Risk (EWMA Analysis)
The EWMA volatility analysis (Figure 1) reveals two distinct volatility patterns that are materially relevant to our firm's equity exposure. First, the March 2020 shock demonstrates the danger of extreme magnitude. Within a matter of weeks, EWMA volatility spiked from a baseline of roughly 0.005 to over 0.05. For an asset management firm, a spike of this size represents immediate, severe drawdowns across client portfolios. The sheer speed of this volatility increase means the firm cannot adjust its risk exposure quickly enough, forcing portfolio managers to either sell assets into a falling market to meet client redemptions or risk breaching internal risk limits.

Second, the 2022–2023 period illustrates the danger of duration. Unlike the sharp shock of 2020, volatility remained persistently elevated (hovering between 0.015 and 0.02) for well over a year. For an asset manager, a prolonged period of high volatility is arguably more damaging than a short spike. It persistently drags down risk-adjusted returns, makes strategic rebalancing expensive, and increases tracking error against benchmarks. This sustained underperformance can ultimately lead to client attrition and reputational damage. The brief 2025 spike serves as a final reminder that volatility regimes can shift rapidly, warning against complacency during periods of market calm.

![Figure 1: EWMA Volatility of S&P 500 Daily Losses (2018-2025)](../figures/ewma_volatility.png)

## 3. Diversification Risk (Stock-Bond Correlation)
The 252-day rolling correlation between the S&P 500 and negative change in the 10-Year Treasury yield (Figure 2) reveals a critical regime shift in how asset interact. From 2008 until 2020, the correlation was predominately negative, frequent hovering between -0.4 and -0.6. For an asset management firm, this validates the traditional 60/40 portfolio strategy: Treasured acted as a reliable haven. When equities sold off, Treasury prices rallied (yield fell), providing a natural hedge that cushioned portfolio drawdowns and dampened overall volatility 

However, beginning in 2021, the correlation sharply reversed into positive territory, peaking above +0.3 in 2022 and 2023. This regime shift was driven by macroeconomic environment of surging inflation and aggressive Federal Reserve rate hikes. For an asset management firm, the implications were severe. A positive correlation meant that stocks and bonds were falling simultaneously. The traditional diversification benefits completely disappeared, and the “safe” fixed-income allocation began amplifying losses rather than cushioning them. While the correlation has recently begun to normalize back toward zero in 2024-2025, the 2022 event serves as a crucial warning: an asset management firm cannot blindly assume that government bonds will always hedge equity risk. Asset allocation must be dynamic and responsive to macroeconomic regimes. 

![Figure 2: 252-Day Rolling Correlation: S&P 500 Returns vs. Negative 10Y Yield Changes](../figures/stock_bond_correlation.png)

## 4. Tail Risk and Model Performance (VaR, ES, and Back-Test)
To quantify the extreme downside risk of our equity exposure, we applied a 1-Day 99% Value at Risk (VaR) and Expected Shortfall (ES) model using Historical Simulation with a 500-day rolling window. Historical simulation is a non-parametric approach that uses the actual distribution of past losses to predict future tail risk. The 99% VaR is defined as the 5th largest loss in the 500-day window, while the 99% ES is the average of the 5 largest losses.

The back-test results for 2018–2025 (Figure 3) show that the model experienced 29 VaR exceptions, compared to an expected number of approximately 20.1 (1% of the 2,010 forecast days). For an asset management firm, this 44% excess in exceptions is highly concerning. It indicates that the model systematically underestimated risk during the most critical periods. 

Furthermore, the exceptions are heavily clustered during specific stress episodes, particularly the March 2020 COVID-19 crash and the 2022 inflation and rate shock. This clustering reveals a critical flaw of historical simulation: it is a reactive model, not a predictive one. As seen in Figure 3, the VaR and ES estimates remain flat before a crisis, and only jump upward *after* the extreme losses have already occurred. For a risk manager, this lag means the model fails exactly when it is needed most—during sudden market drawdowns. Additionally, the 99% ES (the dashed red line) consistently sits above the VaR (the solid blue line), and the gap widens during crises, highlighting that when tail events occur, the average loss is significantly more severe than the VaR threshold itself.

![Figure 3: 1-Day 99% Historical Simulation VaR, ES, and Back-Test (2018-2025)](../figures/var_es_backtest.png)

## 5. Risk Management Implications and Limitations
The primary risk-management implication of this analysis is that an asset management firm can no longer rely on static diversification and backward-looking risk models. The 2022 regime shift proved that a traditional 60/40 portfolio can suffer simultaneous drawdowns in both equities and Treasuries, while the 29 VaR exceptions (versus the 20 expected) proved that 500-day historical simulation lags significantly during sudden market shocks. To address these vulnerabilities, the firm should incorporate forward-looking volatility models (such as EWMA or GARCH) to complement historical simulation. Additionally, portfolio construction must become more dynamic, exploring alternative diversifiers (such as cash, commodities, or trend-following strategies) that do not rely on the historical negative stock-bond correlation.

An important limitation of this analysis is its reliance on historical simulation, which assumes that the past 500 days are representative of the future. It is inherently backward-looking and structurally fails to capture "black swan" events that have no historical precedent. Furthermore, our stock-bond correlation analysis uses the daily change in the 10-year Treasury yield as a proxy for bond returns, rather than actual total return data (which includes coupon income). This proxy may slightly underestimate the true diversification benefit during certain periods.