import pickle
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

## adding the project root so that configs package is available
sys.path.append(str(Path(__file__).resolve().parent.parent))

from configs.system import project_dir

st.set_page_config(page_title='EV Charging Demand Analysis')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


@st.cache_data
def load_all():
    df = pd.read_csv(project_dir.FEATURED_DIR / 'featured_dataset.csv', index_col=0)
    df['StartDay'] = pd.to_datetime(df['StartDay'])
    gb = pickle.load(open(project_dir.MODEL_DIR / 'regression_gb.pkl', 'rb'))
    reg_pre = pickle.load(open(project_dir.MODEL_DIR / 'regressor_preprocessor.pkl', 'rb'))
    rf = pickle.load(open(project_dir.MODEL_DIR / 'classification_rf.pkl', 'rb'))
    clf_pre = pickle.load(open(project_dir.MODEL_DIR / 'classification_preprocessor.pkl', 'rb'))
    return df, gb, reg_pre, rf, clf_pre


df, gb, reg_pre, rf, clf_pre = load_all()
locations = sorted(df['Location'].unique())

min_date = df['StartDay'].min().date()
max_date = df['StartDay'].max().date()

page = st.sidebar.radio('Pages', ['Overview', 'EDA', 'Demand Prediction', 'High-Demand Prediction'])


if page == 'Overview':
    st.title('EV Charging Demand Prediction and Usage Pattern Analysis')
    st.write(f'{len(df):,} charging sessions from {min_date} to {max_date}.')

    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Sessions', f'{len(df):,}')
    c2.metric('Total demand', f"{df['Demand'].sum():,.0f}")
    c3.metric('Avg demand', f"{df['Demand'].mean():.2f}")
    c4.metric('Avg duration', f"{df['Duration'].mean():.0f} min")

    st.subheader('Total demand by location')
    by_location = df.groupby('Location')['Demand'].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(by_location.index, by_location.values)
    ax.invert_yaxis()
    st.pyplot(fig)
    plt.close(fig)

    st.subheader('Average demand by charger type')
    by_type = df.groupby('ChargerType')['Demand'].mean()
    by_type.index = ['Type 0', 'Type 1']
    st.bar_chart(by_type)

    st.subheader('Demand by charger company')
    by_company = df.groupby('ChargerCompany')['Demand'].mean()
    by_company.index = ['Company 0', 'Company 1']
    st.bar_chart(by_company)


elif page == 'EDA':
    st.title('Exploratory Data Analysis')

    st.subheader('Average demand by location')
    by_location = df.groupby('Location')['Demand'].mean().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(by_location.index, by_location.values)
    ax.invert_yaxis()
    st.pyplot(fig)
    plt.close(fig)
    st.write('Accommodation, bus garage and camping have the higher demand per session.')

    st.subheader('Total demand by month')
    by_month = df.groupby(df['StartDay'].dt.month)['Demand'].sum().sort_index()
    by_month.index = [months[int(m) - 1] for m in by_month.index]
    st.bar_chart(by_month)
    st.write('August and July months have the highest demand as per the data.')

    st.subheader('Total demand by days of the week')
    by_day = df.groupby('StartDayOfWeek')['Demand'].sum().reindex(days)
    st.bar_chart(by_day)

    st.subheader('Demand by shift')
    by_shift = df.groupby('Shift')['Demand'].mean().reindex(['Day', 'Night'])
    st.bar_chart(by_shift)
    st.write('In night there is bit high demand as compared to the day timing shift.')

    st.subheader('Duration vs Demand')
    sample = df.sample(n=min(3000, len(df)), random_state=42)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.scatter(sample['Duration'], sample['Demand'], alpha=0.25, s=12)
    ax.set_xlabel('Duration (minutes)')
    ax.set_ylabel('Demand')
    st.pyplot(fig)
    plt.close(fig)

    st.subheader('Average duration by charger company and type')
    st.dataframe(df.groupby(['ChargerCompany', 'ChargerType'])['Duration'].mean().round(1))


elif page == 'Demand Prediction':
    st.title('Charging Demand Prediction')
    st.write('Gradient boosting model from the regression notebook, R2 on test data is 0.79.')

    with st.form('regression form'):
        col1, col2 = st.columns(2)

        with col1:
            location = st.selectbox('Location', locations)
            day = st.selectbox('Day of the week', days)
            shift = st.selectbox('Shift', ['Day', 'Night'])
            month = st.selectbox('Month', months)

        with col2:
            charger_type = st.selectbox('Charger type', ['Type 0', 'Type 1'])
            charger_company = st.selectbox('Charger company', ['Company 0', 'Company 1'])
            duration = st.slider('Duration (minutes)', 0, 1573, 150)

        predict = st.form_submit_button('Predict demand')

    if predict:
        row = pd.DataFrame([{
            'Location' : location,
            'StartDayOfWeek' : day,
            'StartWeek' : days.index(day),
            'StartMonth' : months.index(month) + 1,
            'ChargerCompany' : int(charger_company[-1]),
            'ChargerType' : int(charger_type[-1]),
            'Duration' : duration,
            'Shift' : shift,
        }])

        pred = gb.predict(reg_pre.transform(row))[0]
        st.write('Predicted demand:', round(pred, 2))

    st.subheader('Model comparison')
    ## metrics from the regression notebook
    results = [
        {'model' : 'Linear Regression', 'R2' : 0.5679, 'MAE' : 5.6209, 'MSE' : 77.8578, 'RMSE' : 8.8237},
        {'model' : 'Decision Tree', 'R2' : 0.7555, 'MAE' : 3.5957, 'MSE' : 44.0596, 'RMSE' : 6.6377},
        {'model' : 'Random Forest', 'R2' : 0.7756, 'MAE' : 3.5880, 'MSE' : 40.4315, 'RMSE' : 6.3586},
        {'model' : 'Gradient Boosting', 'R2' : 0.7887, 'MAE' : 3.4831, 'MSE' : 38.0800, 'RMSE' : 6.1709},
        {'model' : 'XGBoost', 'R2' : 0.7989, 'MAE' : 3.3599, 'MSE' : 36.2402, 'RMSE' : 6.0200},
    ]
    st.dataframe(pd.DataFrame(results))
    st.bar_chart(pd.DataFrame(results).set_index('model')['R2'])

    ## shap / lime explanations can be added here


elif page == 'High-Demand Prediction':
    st.title('High-Demand Session Prediction')
    st.write('Random forest from the classification notebook. Median demand (14.1) is the threshold.')

    with st.form('classification form'):
        col1, col2 = st.columns(2)

        with col1:
            shift = st.selectbox('Shift', ['Day', 'Night'])
            location = st.selectbox('Location', locations)
            day = st.selectbox('Day of the week', days)

        with col2:
            charger_type = st.selectbox('Charger type', ['Type 0', 'Type 1'])
            charger_company = st.selectbox('Charger company', ['Company 0', 'Company 1'])
            duration = st.slider('Duration (minutes)', 0, 1573, 150)

        predict = st.form_submit_button('Predict demand category')

    if predict:
        row = pd.DataFrame([{
            'Shift' : shift,
            'Location' : location,
            'ChargerCompany' : int(charger_company[-1]),
            'ChargerType' : int(charger_type[-1]),
            'Duration' : duration,
            'StartDayOfWeek' : day,
        }])

        transformed = clf_pre.transform(row)
        label = rf.predict(transformed)[0]
        prob = rf.predict_proba(transformed)[0][1]

        st.write('Prediction:', 'High Demand' if label == 1 else 'Normal Demand')
        st.write('Probability of high demand:', round(prob, 2))

    st.subheader('Model comparison')
    ## metrics from the classification notebook
    results = [
        {'model' : 'Decision Tree', 'Accuracy' : 0.8913, 'ROC-AUC' : 0.9492, 'F1' : 0.8933, 'Precision' : 0.8774, 'Recall' : 0.9098},
        {'model' : 'Random Forest', 'Accuracy' : 0.8964, 'ROC-AUC' : 0.9558, 'F1' : 0.9003, 'Precision' : 0.8682, 'Recall' : 0.9348},
        {'model' : 'Logistic Regression', 'Accuracy' : 0.8403, 'ROC-AUC' : 0.9125, 'F1' : 0.8441, 'Precision' : 0.8248, 'Recall' : 0.8644},
        {'model' : 'XGBoost', 'Accuracy' : 0.8951, 'ROC-AUC' : 0.9574, 'F1' : 0.8985, 'Precision' : 0.8705, 'Recall' : 0.9284},
        {'model' : 'Gradient Boosting', 'Accuracy' : 0.8896, 'ROC-AUC' : 0.9522, 'F1' : 0.8928, 'Precision' : 0.8681, 'Recall' : 0.9189},
        {'model' : 'LightGBM', 'Accuracy' : 0.8944, 'ROC-AUC' : 0.9571, 'F1' : 0.8980, 'Precision' : 0.8687, 'Recall' : 0.9293},
    ]
    st.dataframe(pd.DataFrame(results))
    st.bar_chart(pd.DataFrame(results).set_index('model')['Accuracy'])

    ## shap / lime explanations can be added here
