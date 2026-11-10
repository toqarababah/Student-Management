import streamlit as st 
st.title("Student Management System")

if "students" not in st.session_state:
    st.session_state["students"] = []

