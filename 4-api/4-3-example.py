import requests
import streamlit as st
import pandas as pd

def get_text_completion(query:str) -> str:
    url = 'https://cent.ischool-iot.net/api/openai/generate'
    data = {'query':query}
    headers = {'X-API-KEY':'4545dc7870b41b6d4971c147'}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    return response.json()

st.title("FIRST GPT API INTERACTION")
text = st.text_area("Enter text")

if text: 
    with st.spinner("Thinking..."):

        response = get_text_completion(text)
        st.write(response)