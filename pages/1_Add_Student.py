import streamlit as st 
st.header("Add a New Student")

student_name =st.text_input("Student Name")
student_major = st.text_input("Major")

if st.button("Save"):
    # إضافة البيانات إلى الذاكرة
    st.session_state["students"].append({"name": student_name, "major": student_major})
    st.success(f"Student {student_name} added successfully!")