import streamlit as st

st.title("Area and perimeter calculator")

length = st.number_input("Enter the length of the rectangle")
width = st.number_input("Enter the width of the rectangle")

area = length * width
perimeter = 2 * (length + width)
if perimeter:
    st.write(f"The area of the rectangle is {area} and the perimeter {perimeter}")