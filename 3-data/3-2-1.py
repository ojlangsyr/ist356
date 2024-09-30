'''
Read this file into a pandas dataframe:

[https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log](https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log)

- What is the delimiter? " "
- is there a header? Which row?
- Do you need to skip lines?

Display only data where the time taken > 500 (msec) and the sc-status is 200

as a streamlit
'''

import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log", sep=" ", header=3)
filtered_df = df[(df["time-taken"] > 500) & (df["sc-status"] == 200)]
st.write(filtered_df)
