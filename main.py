import streamlit as st

st.set_page_config(layout="wide")

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                            ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} day(s) in {place}")

chart = st.plotly_chart()
