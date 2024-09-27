import mysql.connector
import streamlit as st
import pandas as pd

con = mysql.connector.connect(
  host="localhost",
  port="33061",
  user="root",
  password="c6h5bwInqtKJKmiuPcBQ0A",
  database="censo"
)

cur = con.cursor()

cur.execute("select * from Escola limit 20")
rows = cur.fetchall()

st.header("Escolas")
st.write(rows)