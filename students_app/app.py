import streamlit as st
import database as db
from views import student_form, admin_dashboard

st.set_page_config(page_title='Student Portal', layout='wide')

def main():
    db.init_db()

    page = st.sidebar.radio('Navigate', ['Student Registration', 'Admin Dashboard'])

    if page == 'Student Registration':
        student_form.show_student_page()
    else:
        admin_dashboard.show_admin_page()

if __name__ == '__main__':
    main()