# EV Charging Demand Prediction and Usage Pattern Analysis

Predicts EV charging demand and classifies high-demand sessions using charger type,
location, company, and time features.

## Tech Stack

Python, Scikit-learn, XGBoost, LightGBM, Statsmodels, SHAP, Streamlit, Poetry

## Setup

```bash
poetry install
```

## Run

```bash
poetry run streamlit run streamlit/app.py
```

## Structure

- `data-preprocessing/` — cleaning + feature engineering
- `eda/` — EDA notes
- `regression/` — demand prediction (best R²: 0.7989, XGBoost)
- `classification/` — high vs normal demand (best ROC-AUC: 0.9574, XGBoost)
- `time-forecasting/` — daily demand forecast
- `streamlit/` — dashboard
- `models/` — pickled models
