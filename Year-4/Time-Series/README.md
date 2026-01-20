# Time Series

This repository contains the statistical analysis of a univariate time series, focusing on the **Box-Jenkins methodology** for ARIMA modeling.

## Project Overview: Univariate Forecasting
The project involved a comprehensive study of a real-world time series, covering the following phases:

1. **Descriptive Analysis:** Study of stationarity, seasonality, and variance stability (Box-Cox transformations).
2. **Identification:** Analysis of ACF and PACF plots to identify potential AR, MA, or ARIMA candidates.
3. **Estimation & Selection:** Model fitting and comparison using information criteria (**AIC, BIC**).
4. **Diagnosis:** Residual analysis (Ljung-Box test, normality, homoscedasticity) to ensure model validity.
5. **Forecasting:** Predicting future values with confidence intervals.

## Tech Stack
* **Language:** R
* **Format:** Jupyter Notebook
* **Key Libraries:** `tseries`, `forecast`, `ggplot2`.

## Deliverables
* **Analysis Notebook:** Complete code with step-by-step statistical reasoning.
* **Final Presentation (PDF):** A technical slide deck summarizing the findings, model selection process, and 12-month predictions.

## AI Relevance
* **Sequential Data:** Understanding time series is the precursor to working with Recurrent Neural Networks (**RNNs**), **LSTMs**, and **Transformers** for forecasting.
* **Statistical Rigor:** Mastery of stationarity and seasonality is essential for feature engineering in any machine learning model dealing with temporal data.
