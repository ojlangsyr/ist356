import requests
import pandas as pd
import streamlit as st
from fastapi import FastAPI, Header, Query
import json

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/flights/sample-flights.csv"
df = pd.read_csv(url)

app=FastAPI()
@app.get("/api/flights/search")
def search_flights(type:str = Query(),code:str = Query()):
    #departure_airport_code
    #arrival_airport_code

    if type == 'dep':
        flights = df[df['departure_airport_code'] == code]
    elif type == 'arr':
        flights = df[df['arrival_airport_code'] == code]
    else:
        return{}

    json_flights = flights.to_json(orient="records")
    return json.loads(json_flights)


