import streamlit as st
import pandas as pd
from utils.weather_api import get_forecast

st.title("📈 5-Day Forecast Analytics")

city = st.text_input("Enter City")

if st.button("Show Forecast"):
    with st.spinner("Fetching forecast..."):
        times, temps = get_forecast(city)

    if temps:
        df = pd.DataFrame({
            "Time": pd.to_datetime(times),
            "Temperature": temps
        })

        st.subheader("📊 Temperature Trend")
        st.line_chart(df.set_index("Time"))

        st.subheader("📌 Insights")
        st.write("Average Temp:", sum(temps)//len(temps))
        st.write("Max Temp:", max(temps))
        st.write("Min Temp:", min(temps))

    else:
        st.error("Forecast data not available")