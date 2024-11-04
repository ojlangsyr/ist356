import streamlit as st
import pandas as pd
import requests


key = "4545dc7870b41b6d4971c147"


def open_complete(prompt):
    params = {"temperature":0}
    url = "https://cent.ischool-iot.net/api/openai/generate"
    headers = {"X-API-KEY":"4545dc7870b41b6d4971c147"}
    data = {'query':prompt}
    response = requests.post(url, headers=headers,data=data,params=params)
    response.raise_for_status()
    return response.json()

def spellcheck (test):
    prompt = "Please spell check the following text: \n"
    prompt += text + "\n"
    prompt += "for each misspelled word, provide one suggested correction"
    prompt += "return these as a list of dictionary in JSON format \n"
    response = open_complete(prompt)
    return response


st.title("LLM Spell Check")
text = st.text_input("Enter text to spellcheck")
response = spellcheck(text)
st.write(response)