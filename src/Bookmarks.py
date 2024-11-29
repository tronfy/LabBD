import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode

import mysql.connector

st.header("Bookmarks")

conn = mysql.connector.connect(
  host=st.secrets.DB_HOST,
  user=st.secrets.DB_USERNAME,
  password=st.secrets.DB_PASSWORD,
  port=3306,
  database=st.secrets["DB_NAME"],
  auth_plugin="mysql_native_password",
)

cur = conn.cursor(buffered=True)

cur.execute("select e.CO_ENTIDADE as id, e.NO_ENTIDADE as nome from escola e inner join bookmark b on e.CO_ENTIDADE = b.id_entidade where b.id_usuario=%s", (st.session_state["user_id"],))
bookmarks = cur.fetchall()
df = pd.DataFrame(bookmarks, columns=cur.column_names)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(selection_mode="single")
gb.configure_side_bar()
gridOptions = gb.build()

data = AgGrid(
  df,
  gridOptions=gridOptions,
  enable_enterprise_modules=True,
  allow_unsafe_jscode=True,
  update_mode=GridUpdateMode.SELECTION_CHANGED,
  columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
)

selected = data["selected_rows"]

if selected is not None and len(selected) > 0:
  st.session_state["id_escola"] = selected.values[0][0]
  st.switch_page("EscolaDetalhes.py")
