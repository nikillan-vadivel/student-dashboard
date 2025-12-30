import streamlit as st
import database as db

def show_student_page():
    st.title('Student Registration Form')
    st.write('Please enter your details')

    with st.form('registration_form', clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input('Full name')
            age = st.slider('Age', 16, 30, 18)
            gender = st.radio('Gender', ['Male', 'Female', 'Other'], horizontal=True)

        with col2:
            state = st.selectbox('State',["Tamil Nadu", "Kerala", "Karnataka", "Maharashtra", "Delhi", "Other"])
            subjects = st.multiselect("Select Subjects", ["Math", "Physics", "Chemistry", "CS", "Biology", "English"])

        submitted = st.form_submit_button('Submit Registration')

        if submitted:
            if name and subjects:
                # Call the backend function
                db.add_student(name, age, gender, state, subjects)
                st.success(f"Thank you, {name}! Your data has been recorded.")
                st.balloons()
            else:
                st.error("Please enter your name and select at least one subject.")