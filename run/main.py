import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")

# add title, text input, slider, selectbox, subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} day(s) in {place}")

if place:
    try:
        # get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            temperatures = [round(temperature, 2) for temperature in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure, use_container_width=True)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.error("Non-existing place is entered")
