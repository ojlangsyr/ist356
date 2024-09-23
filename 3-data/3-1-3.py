import pandas as pd
import numpy as np
import streamlit as st


st.title("Challenge 3-1-3")


customers=pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv")
gend = st.radio("Select a gender", ["M", "F"])
if gend == "M":
    st.write(customers[customers['Gender'] == "M"])
elif gend == "F":
    st.write(customers[customers['Gender'] == "F"])
