import mysql.connector
import streamlit as st
import pandas as pd

USE_DOCKER = True

con = mysql.connector.connect(
    host="localhost",
    port="33061" if USE_DOCKER else "3306",
    user="root",
    password="c6h5bwInqtKJKmiuPcBQ0A" if USE_DOCKER else "aluno",
    database="censo" if USE_DOCKER else "labbd",
)

cur = con.cursor()

cur.execute("select CO_ENTIDADE, NO_ENTIDADE from Escola limit 20")
rows = cur.fetchall()

rows = pd.DataFrame(rows, columns=["CO_ENTIDADE", "NO_ENTIDADE"])

st.header("Escolas")
st.write(rows)
