import streamlit as st
import pydeck as pdk
from utils.weather_api import get_current_weather
from utils.location import get_location

st.title("🌤️ Current Weather")

city = st.text_input("Enter City", value=get_location())

if st.button("Get Weather"):
    with st.spinner("Fetching weather data..."):
        data = get_current_weather(city)

    if data:
        col1, col2 = st.columns(2)

        icon_url = f"http://openweathermap.org/img/wn/{data['icon']}@2x.png"

        with col1:
            st.image(icon_url)
            st.metric("Temperature", f"{data['temp']} °C")
            st.metric("Condition", data['condition'])

        with col2:
            st.metric("Humidity", f"{data['humidity']}%")
            st.metric("Wind", f"{data['wind']} m/s")
            st.metric("Pressure", f"{data['pressure']} hPa")

        st.write("Description:", data['description'])

        # 🗺️ Map
        st.subheader("📍 Location Map")

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=[{"lat": data["lat"], "lon": data["lon"]}],
            get_position="[lon, lat]",
            get_radius=50000,
        )

        view = pdk.ViewState(
            latitude=data["lat"],
            longitude=data["lon"],
            zoom=5
        )

        st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view))

    else:
        st.error("Invalid city or API issue")