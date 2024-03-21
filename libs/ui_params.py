import streamlit as st
from libs.constants import *
from libs.dot_dict_class import DotDict


def format_crypto(x):
    if x is None:
        return CRYPTOS[x]
    else:
        return x + " - " + CRYPTOS[x]


def create_ui_params():
    st.title("Market Forecast")
    st.caption("Raw data is extracted from `Yahoo! Finance`.")
    st.caption("The app usage is tracked using [statcounter.com](https://statcounter.com/),"
               " and it does not contain any personal information, since we never ask you any personal info."
               " By using this app, you agreed with these terms and conditions.")
    st_ml_model = st.sidebar.selectbox("Predictive Model", options=list(ML_MODELS.keys()), index=0,
                                       format_func=lambda x: ML_MODELS[x])
    st_crypto_stock = st.sidebar.radio("Symbol Type", options=TICKER_TYPE)

    st_crypto_name = st.sidebar.selectbox("Crypto Symbol", options=list(CRYPTOS.keys()),
                                            format_func=format_crypto)
    st_currency_name = st.sidebar.selectbox("Currency", options=CURRENCIES)

    if st_crypto_name is None:
        st_ticker_name = None
    else:
        st_ticker_name = st_crypto_name + "-" + st_currency_name
            
    st_period = st.sidebar.selectbox("Period (History)", options=list(PERIODS.keys()), index=7,
                                     format_func=lambda x: PERIODS[x])
    st_interval = st.sidebar.selectbox("Interval", options=list(INTERVALS.keys()), index=8,
                                       format_func=lambda x: INTERVALS[x]) 
    st_price_column = st.sidebar.selectbox("Price",
                                           options=TICKER_DATA_COLUMN,
                                           index=3)
    st_future_days = st.sidebar.number_input("Future Days", value=365, min_value=1, step=1)
    st_future_volume = st.sidebar.number_input("Future Volume Assumption", value=0, min_value=0, step=1)
    st.sidebar.caption("Set Volume to 0 to ignore")
    st_training_percentage = st.sidebar.slider("Training Percentage", min_value=0.0, max_value=1.0, step=0.1, value=0.8)
    st_yearly_seasonality = st.sidebar.selectbox("Yearly Seasonality",
                                                 options=SEASONALITY_OPTIONS,
                                                 index=0)
    st_weekly_seasonality = st.sidebar.selectbox("Weekly Seasonality",
                                                 options=SEASONALITY_OPTIONS,
                                                 index=0)
    st_daily_seasonality = st.sidebar.selectbox("Daily Seasonality",
                                                options=SEASONALITY_OPTIONS,
                                                index=0)
    st_holidays = st.sidebar.selectbox("Holidays", options=list(HOLIDAYS.keys()), index=0,
                                       format_func=lambda x: HOLIDAYS[x])

    if st_crypto_stock == TICKER_TYPE[0]:
        st_seasonality_mode_index = 0
    else:
        st_seasonality_mode_index = 1
    st_seasonality_mode = st.sidebar.selectbox("Seasonality Mode",
                                               options=SEASONALITY_MODE_OPTIONS,
                                               index=st_seasonality_mode_index)

    dic_return = DotDict(model=st_ml_model,
                         ticker_name=st_ticker_name,
                         period=st_period,
                         interval=st_interval,
                         future_days=st_future_days,
                         price_column=st_price_column,
                         future_volume=st_future_volume,
                         training_percentage=st_training_percentage,
                         yearly_seasonality=st_yearly_seasonality,
                         weekly_seasonality=st_weekly_seasonality,
                         daily_seasonality=st_daily_seasonality,
                         holidays=st_holidays,
                         seasonality_mode=st_seasonality_mode)
    return dic_return
