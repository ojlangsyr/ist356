'''
Write a streamlit accept an Excel file via file uploader and then writes out a record-oriented JSON file from the first tab in the excel file.

The program should display the contents of the dataframe and provide a download button for the converted the csv file. 


Advice:

 - https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
 - https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
'''
import streamlit as st
import pandas as pd

file=st.file_uploader("Upload a file", type=["xlsx"])

df=pd.read_excel(file)
df=df.to_json(orient="records")

st.write(df)

st.download_button(df   )