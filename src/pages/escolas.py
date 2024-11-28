import mysql.connector
import streamlit as st
import pandas as pd

conn = mysql.connector.connect(
  host=st.secrets.DB_HOST,
  user=st.secrets.DB_USERNAME,
  password=st.secrets.DB_PASSWORD,
  port=3306,
  database=st.secrets["DB_NAME"],
  auth_plugin="mysql_native_password",
)

cur = conn.cursor()

cur.execute("select NO_ENTIDADE as nome, TP_SITUACAO_FUNCIONAMENTO as status, CO_MUNICIPIO as municipio, TP_LOCALIZACAO as localizacao, TP_DEPENDENCIA as dependencia from escola;")
rows = cur.fetchall()

rows = pd.DataFrame(rows, columns=cur.column_names)

st.header("Escolas")
st.write(rows)
