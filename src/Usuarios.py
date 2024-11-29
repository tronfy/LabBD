import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import mysql.connector

st.header("Usuários")

conn = mysql.connector.connect(
  host=st.secrets.DB_HOST,
  user=st.secrets.DB_USERNAME,
  password=st.secrets.DB_PASSWORD,
  port=3306,
  database=st.secrets["DB_NAME"],
  auth_plugin="mysql_native_password",
)

cur = conn.cursor(buffered=True)

cur.execute("select id_usuario as id, nome, email, case when gerencial = 1 then '✅' else '❌' end as gerencial, data_nascimento from usuario")

usuarios = cur.fetchall()
df = pd.DataFrame(usuarios, columns=cur.column_names)

AgGrid(df)
