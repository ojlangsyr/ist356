import streamlit as st
import pandas as pd
import requests

st.title("Weather")
#get geolocation from search
'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=Syracuse%20New%20York' \
  -H 'accept: application/json'
'''

location = st.text_input("Enter a location")



if st.button("Get Weather"):
    url = "https://cent.ischool-iot.net/api/google/geocode"
    params = {"location":location}
    headers = {"X-API-KEY":"ea044c96950db6cc0fab7ae1"}
    response = requests.get(url,params=params, headers=headers)
    response.raise_for_status()
    geocode = response.json()
    #st.write(geocode)
    lon = geocode["results"][0]["geometry"]["location"]["lng"]
    lat = geocode["results"][0]["geometry"]["location"]["lat"]

    


    url = "https://cent.ischool-iot.net/api/weather/current"
    params = {"units":"imperial", "lon":lon,"lat":lat}
    response = requests.get(url,params=params,headers=headers)

    response.raise_for_status()
    weather = response.json()
    temp = weather["current"]["temperature_2m"]
    st.metric("Temperature: ",temp)