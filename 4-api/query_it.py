import pandas as pd
import requests 
import streamlit as st

APIKEY = "4545dc7870b41b6d4971c147"

st.title("Query It!")

file = st.file_uploader("Upload a csv file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)

    question = st.text_area("What question would you like to ask of this data?")
    if question:
        prompt = "With the following data:\n"
        prompt += df.to_string(index=False)
        prompt += "\n\n"
        prompt += "Answer the following question:\n"
        prompt += question

        url = "https://cent.ischool-iot.net/api/openai/generate"
        response = requests.post(url, data={"query": prompt}, headers={"x-api-key" : APIKEY})
        response.raise_for_status()
        results = response.json()
        st.write(results)
  
  