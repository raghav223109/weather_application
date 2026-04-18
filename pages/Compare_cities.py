import streamlit as st
from utils.weather_api import get_current_weather

st.title("🌍 Compare Cities")

cities = st.text_input("Enter cities (comma separated)", "Delhi, Mumbai, Bangalore")

if st.button("Compare"):
    city_list = [c.strip() for c in cities.split(",") if c.strip()]

    cols = st.columns(len(city_list))

    for i, city in enumerate(city_list):
        with cols[i]:
            st.subheader(city)

            with st.spinner("Loading..."):
                data = get_current_weather(city)

            if data:
                st.metric("Temp", f"{data['temp']}°C")
                st.metric("Humidity", f"{data['humidity']}%")
                st.metric("Wind", f"{data['wind']} m/s")
            else:
                st.error("Error")