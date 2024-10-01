import pandas as pd
import streamlit as st
import requests
employees = requests.get("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json")
employees = employees.json()
dflist=[]
for key in employees.keys():
    df=pd.DataFrame(employees[key])
    df['department'] = key
    dflist.append(df)

combineddf=pd.concat(dflist)
st.dataframe(combineddf)
