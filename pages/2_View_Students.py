import streamlit as st
st.header("View All Students")

# نتحقق إذا كانت القائمة موجودة وتحتوي على بيانات
if "students" not in st.session_state or len(st.session_state["students"]) == 0:
    st.info("No students added yet. Go to 'Add Student' page to add some!")
else:
    # عرض البيانات على شكل جدول
    st.dataframe(st.session_state["students"], use_container_width=True)