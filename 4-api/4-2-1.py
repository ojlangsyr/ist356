'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 4545dc7870b41b6d4971c147' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=The%20pizza%20is%20great.%20The%20customer%20service%20was%20not.'
'''

import requests
import streamlit as st
import pandas as pd

def extract_entities(text:str) -> dict:
    url = 'https://cent.ischool-iot.net/api/azure/entityrecognition'
    headers = {'X-API-KEY':'4545dc7870b41b6d4971c147'}
    data = {'text':text}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()



text = st.text_area("Enter text")
if text:
    result = extract_entities(text)
    entities= result['results']['documents'][0]['entities']
    df=pd.DataFrame(entities)
    st.dataframe(df)

