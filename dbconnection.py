import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Function to connect to SQL Server and retrieve data based on user role and table
def get_data(user_role, table_name):
    # Replace 'your_server', 'your_database', 'your_username', and 'your_password' with your SQL Server details
    conn_str = 'mssql+pyodbc://Mydeb:jamali 13@HASSAN-JAWAD\\SQLEXPRESS01/Jawad?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(conn_str)



    # Customize the SQL query based on user role and table name
    query = f'SELECT * FROM {table_name}'

    # Fetch data using pandas
    data = pd.read_sql(query, engine)

    return data

# Streamlit app
def main():
    st.title("ASSIGNMENT UPLOADER WEBSITE BY HASSAN JAWAD")

    # Sidebar for user selection
    user_role = st.sidebar.selectbox("Select User Role", ['Admin', 'Student', 'Teacher'])

    # Sidebar for table selection
    table_name = st.sidebar.selectbox("Select Table", ['student', 'submission', 'Courses', 'assignment'])

    # Get data based on user role and table name
    data = get_data(user_role, table_name)

    # Display the data
    st.write(f"Data for {user_role} user from {table_name} table:")
    st.dataframe(data)

# Run the app
if __name__ == "__main__":
    main()
