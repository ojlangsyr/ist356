import pandas as pd
import numpy as np
import streamlit as st

customers=pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv")
desc=customers.describe()
st.write(desc)

headtail = st.radio("Select head or tail", ["HEAD", "TAIL"])
if headtail == "HEAD":
    st.write(customers.head())
elif headtail == "TAIL":
    st.write(customers.tail())

