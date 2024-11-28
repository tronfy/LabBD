import mysql.connector
import streamlit as st
# from st_aggrid import AgGrid, JsCode, GridOptionsBuilder
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
  n_matriculas, n_docentes, n_turmas
from escola e
  inner join cat_situacao on e.TP_SITUACAO_FUNCIONAMENTO = cat_situacao.id
  inner join cat_municipio on e.CO_MUNICIPIO = cat_municipio.id
  inner join cat_localizacao on e.TP_LOCALIZACAO = cat_localizacao.id
  inner join cat_dependencia on e.TP_DEPENDENCIA = cat_dependencia.id
  inner join escola_matriculas em on e.CO_ENTIDADE = em.CO_ENTIDADE
  inner join escola_docentes ed on e.CO_ENTIDADE = ed.CO_ENTIDADE
  inner join escola_turmas et on e.CO_ENTIDADE = et.CO_ENTIDADE
order by n_matriculas desc
;""")
rows = cur.fetchall()
conn.close()

df = pd.DataFrame(rows, columns=cur.column_names)

# add page link to details page, use st.page_link
# df['nome'] = df['nome'].apply(lambda x: f"[{x}](http://localhost:8051/Detalhes_-_Escola/?id={x})")
df['id'] = df['id'].apply(lambda x: f"/EscolaDetalhes/?id={x}")

# gb = GridOptionsBuilder.from_dataframe(df)
# gb.configure_column("detalhes", cellRenderer=JsCode("function(params) {return '<a href=' + params.value + '>link</a>'}"))
# gridOptions = gb.build()

st.header("Escolas")
st.data_editor(
    df,
    column_config={
        # "id": st.column_config.LinkColumn("id", display_text="/Detalhes_-_Escola/?id=(.*?)"),
        "id": st.column_config.LinkColumn("detalhes", display_text="link"),

    },
    hide_index=True,
)

# st.write(df)
# AgGrid(df, gridOptions=gridOptions, allow_unsafe_jscode=True)
