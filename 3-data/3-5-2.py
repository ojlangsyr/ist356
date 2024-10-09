'''
Let's build an interactive pivot table in streamlit!

- create a row and column selection widgets allowing the user to select one of the following columns:  
`'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade'`
- create a measure column selestion widget which allows the user to select one of these columns:  
`'Completion_Time','Student_Score'`
- build the pivot table dataframe from the inputs. use the average for the `aggfunc`
- display the pivot table!

**EXTRA CHALLENGE:** Do not allow the name value in row and column!
'''
import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv")

st.title('Interactive Pivot Table')
choices = [ 'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
selection1 = st.selectbox('Select a column for rows', choices)
choices1 = ['Completion_Time','Student_Score']
selection2 = st.selectbox('Select a measure column', choices1)

pivot = pd.pivot_table(df, index=selection1, values=selection2, aggfunc='mean')

st.dataframe(pivot)