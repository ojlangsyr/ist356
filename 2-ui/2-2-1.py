import streamlit as st


#initialize session state 
if 'length' not in st.session_state:
    st.session_state.length = 0
if 'width' not in st.session_state:
    st.session_state.width = 0

st.title("Area and perimeter calculator")

length = st.number_input("Enter the length of the rectangle", value = st.session_state.length)   # defaults come from the session state
width = st.number_input("Enter the width of the rectangle", value = st.session_state.width)
btn_clicked = st.button("Calculate")
btn_clear= st.button("Clear")

# checks for click
if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"The area of the rectangle is {area} and the perimeter {perimeter}")

# reset clear session state (set to none)
if btn_clear:
    st.session_state.length = None
    st.session_state.width = None
    st.rerun()