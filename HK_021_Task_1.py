import requests
import streamlit as st
import pandas as pd

st.title("Pollution Concentration Dashboard")

lat = st.number_input("Enter Latitude", value=19.0760)
lon = st.number_input("Enter Longitude", value=72.8777)

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

if st.button("Check Pollution"):
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(url)
    
    if res.status_code == 200:
        data = res.json()
        if "list" in data and len(data["list"]) > 0:
            pollutants = data["list"][0]["components"]
            aqi = data["list"][0]["main"]["aqi"]
            pollutants["AQI"] = aqi
            df = pd.DataFrame([pollutants])
            st.dataframe(df)
        else:
            st.error(f"No data available: {data.get('message', 'Unknown error')}")
    else:
        st.error(f"Request failed with status code {res.status_code}")







