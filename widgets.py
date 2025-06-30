import streamlit as st

st.title("Widgets Example")

name = st.text_input("Enter your name")

if name:
        st.write(f"Hello, {name}!")

age = st.slider("select your age", 0 , 100,25)
if age:
    st.write(f"You are {age} years old.")


options = ["NC", "AZ", "GA"]

state = st.selectbox("select your state", options)
if state:
    st.write(f"You selected {state}.")