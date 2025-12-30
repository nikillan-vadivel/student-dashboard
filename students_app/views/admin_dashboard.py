import streamlit as st
import plotly.express as px
import database as db

ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD")

@st.dialog('Confirm Deletion')
def confirm_delete_dialog(student_id):
    st.write(f'Are you sure you want to permanently delete Student ID **{student_id}**')
    st.warning('This action cannot be undone.')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Cancel', width='stretch'):
            st.rerun()
        
    with col2:
        if st.button('Delete', type = 'primary', width='stretch'):
            db.delete_student(student_id)
            st.success('Deleted')
            st.rerun()

def show_admin_page():
    st.title('Admin Dashboard')

    password = st.sidebar.text_input('Admin Password', type='password')

    if password == ADMIN_PASSWORD:
        st.success("Access Granted")

        df = db.get_all_students()

        if not df.empty:
            tab1, tab2 = st.tabs([
                'Data Management',
                "Visualizations"
            ])

            with tab1:
                st.subheader('Students Database')
                st.dataframe(df, width='stretch')

                st.divider()
                st.warning('Delete Zone!!')

                col_input, col_btn = st.columns([3,1])
                with col_input:
                    id_to_delete = st.number_input('Enter ID to delete', min_value=1)
                
                with col_btn:
                    st.write("")
                    st.write("")
                    if st.button('Delete Record'):
                        confirm_delete_dialog(id_to_delete)

            with tab2:
                st.subheader('Analytics Overview')
                col_chart1, col_chart2 = st.columns(2)

                with col_chart1:
                    st.write('Gender Ratio')
                    fig_gender = px.pie(df, names='gender', title='Gender Distribution', hole=0.3)
                    st.plotly_chart(fig_gender, width='stretch')

                with col_chart2:
                    st.write('Students per State')
                    state_counts = df['state'].value_counts().reset_index()
                    state_counts.columns = ['state','count']
                    fig_state = px.bar(state_counts, x='state', y='count',
                                        title='Enrollment by state', color='count')
                    st.plotly_chart(fig_state, width='stretch')

        else:
            st.info('No records found in DB yet')
        
    else:
        if password:
            st.error('Incorrect Password')
        st.info('Please enter the admin password in the sidebar')