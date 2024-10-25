import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host=st.secrets.DB_HOST,
    user=st.secrets.DB_USERNAME,
    password=st.secrets.DB_PASSWORD,
    port=3306,
    database=st.secrets["DB_NAME"],
    auth_plugin="mysql_native_password",
)
