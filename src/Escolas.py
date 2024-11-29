import mysql.connector
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
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

cur.execute("""
select
  e.CO_ENTIDADE as id,
  e.NO_ENTIDADE as nome,
  cat_situacao.descricao as status,
  cat_municipio.nome as municipio,
  cat_localizacao.descricao as localizacao,
  cat_dependencia.descricao as dependencia,
  case when e.IN_COMUM_PRE = 1 then '✅' else '❌' end as nivel_EI,
  case when e.IN_COMUM_FUND_AI = 1 then '✅' else '❌' end as nivel_EF1,
  case when e.IN_COMUM_FUND_AF = 1 then '✅' else '❌' end as nivel_EF2,
  case when e.IN_COMUM_MEDIO_NORMAL = 1 then '✅' else '❌' end as nivel_EM,
  case when e.IN_EJA = 1 then '✅' else '❌' end as nivel_EJA,
  case when e.IN_PROFISSIONALIZANTE = 1 then '✅' else '❌' end as nivel_EP,
  case when e.IN_ESPECIAL_EXCLUSIVA = 1 then '✅' else '❌' end as nivel_EE,
  n_matriculas, n_docentes, n_turmas,
  g.LAT as latitude, g.LON as longitude
from escola e
  inner join cat_situacao on e.TP_SITUACAO_FUNCIONAMENTO = cat_situacao.id
  inner join cat_municipio on e.CO_MUNICIPIO = cat_municipio.id
  inner join cat_localizacao on e.TP_LOCALIZACAO = cat_localizacao.id
  inner join cat_dependencia on e.TP_DEPENDENCIA = cat_dependencia.id
  inner join escola_matriculas em on e.CO_ENTIDADE = em.CO_ENTIDADE
  inner join escola_docentes ed on e.CO_ENTIDADE = ed.CO_ENTIDADE
  inner join escola_turmas et on e.CO_ENTIDADE = et.CO_ENTIDADE
  inner join geolocalizacao g on e.CO_ENTIDADE = g.CO_ENTIDADE
order by n_matriculas desc
;""")
rows = cur.fetchall()
conn.close()

df = pd.DataFrame(rows, columns=cur.column_names)

# add page link to details page, use st.page_link
# df['nome'] = df['nome'].apply(lambda x: f"[{x}](http://localhost:8051/Detalhes_-_Escola/?id={x})")
# df['id'] = df['id'].apply(lambda x: f"/EscolaDetalhes/?id={x}")

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(selection_mode="single")
gb.configure_side_bar()
gridOptions = gb.build()

st.header("Escolas")
st.write("Selecione uma escola para ver detalhes")


if "user_role" in st.session_state and st.session_state["user_role"] == "gerencial":
  st.download_button("Baixar escolas.csv", df.to_csv(), "escolas.csv", "text/csv")

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

st.map(df)
