import streamlit as st
import plotly.express as px

# st.set_page_config(layout="wide")

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} day(s) in {place}")

dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
temperatures = [10, 11, 15]
temperatures = [days * i for i in temperatures]

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
