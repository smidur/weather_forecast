import streamlit as st

st.set_page_config(layout="wide")

st.title("Weather Forecast for the Next Days")

city = st.text_input("Place")

forecast_days = st.select_slider("Forecast Days", range(1, 6))

data_to_view = st.selectbox("Select data to view")

st.header(f"Temperature for the next {forecast_days} day(s) in {city}")

chart = st.plotly_chart()
