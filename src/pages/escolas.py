import mysql.connector
import streamlit as st
import pandas as pd

from sql import conn

cur = conn.cursor()

cur.execute("select * from escola;")
rows = cur.fetchall()

rows = pd.DataFrame(rows, columns=cur.column_names)

st.header("Escolas")
st.write(rows)
