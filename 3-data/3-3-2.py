import streamlit as st
import requests
import pandas as pd

customers = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/customers.csv")


months=['jan','feb','mar','apr']
months_df=[]
for month in months:
    month_df = pd.read_csv(f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/purchases-{month}.csv")
    months_df['month'] = month
    months_df.append(month_df)

purchases=pd.concat(months_df)

combined=pd.merge(customers, purchases, on='customer_id', how='left')


selectedmonth = st.selectbox('Select Month', months)
filtered = combined[combined['month'] == selectedmonth]

no_purchase = combined[combined['order_id'].isnull()]
st.dataframe(filtered)