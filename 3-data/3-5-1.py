'''
Create a streamlit to allow the user to select one of the following:

- one of: Made_Own_Study_Guide, Did_Exam_Prep Assignment, Studied_In_Groups	
- after the selection is made display a dataframe that summarized the count of students and the average student score by the selection
'''
import streamlit as st
import pandas as pd

st.title('Display data')

df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv")

choices = ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']
selection = st.selectbox('Select a column', choices)

grouped = df.groupby(selection).agg({'Student_Score': ['count', 'mean']})
st.dataframe(grouped)