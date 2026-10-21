# EV Charging Demand Prediction and Usage Pattern Analysis

Completed end-to-end data science project for analyzing EV charging usage, predicting session-level demand, classifying high-demand sessions, and forecasting daily demand.

## Features
- Data cleaning, exploratory data analysis (EDA), and feature engineering across charging-session, charger, location, company, duration, and time-related variables.
- Regression models to predict demand for an individual charging session. Best reported result: **XGBoost R² = 0.7989**.
- Classification models to identify high-demand versus normal-demand sessions. Best reported result: **XGBoost ROC-AUC = 0.9574**.
- Daily time-series demand forecasting, including trend/seasonality analysis and a 7-day moving-average baseline evaluated using MAE.
- Interactive Streamlit dashboard with filters and pages for overview, EDA, demand prediction, and high-demand prediction.
- Saved models and preprocessing pipelines used by the dashboard.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, LightGBM, Statsmodels, SHAP, Streamlit, Poetry

## Run
```bash
poetry install
poetry run streamlit run streamlit/app.py
```

## Project Structure
- `data-preprocessing/` — data overview, cleaning, and feature engineering
- `eda/` — exploratory analysis
- `regression/` — demand prediction and model evaluation
- `classification/` — high-demand session classification and model evaluation
- `time-forecasting/` — daily demand forecasting
- `streamlit/` — interactive dashboard
- `models/` — serialized models and preprocessors
- `configs/` — project path configuration

## Repository
https://github.com/blu3-bird/EV-demand
