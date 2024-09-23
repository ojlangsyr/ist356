import streamlit as st

if 'history' not in st.session_state:
    st.session_state.history = []
if 'total' not in st.session_state:
    st.session_state.total = 0

st.title("Add a number")
num = st.number_input("Enter a number")
add = st.button("Add number") 
btn_clear = st.button("Clear")

history = []

if add:
    st.session_state.total = st.session_state.total + num
    st.write(f"Total: {st.session_state.total}")
    st.session_state.history.append(num)
    st.write(f"History: {st.session_state.history}")


if btn_clear:
    st.session_state.num = 0
    st.session_state.history = []
    st.session_state.total = 0
    st.rerun()



