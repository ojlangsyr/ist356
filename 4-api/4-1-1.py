import requests
import pandas as pd
import streamlit as st
url = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(url)
response.raise_for_status()
users = response.json()
users = pd.json_normalize(users)



st.title("First API")
st.dataframe(users)