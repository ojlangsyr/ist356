import streamlit as st

st.title("GPA CALC")


name= st.text_input("What is your name? ")
major = st.radio("Select your major:", ("IMT Major", "IST Major", "ADA Major"))
gpa = st.number_input("What is your GPA?")



if gpa < 1.8:
    status = "probation"
elif gpa > 3.4:
    status = "deans list"
else:
    status = "no list"

st.write(f"{name} in {major} with {gpa} is on {status}")