import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
  host=st.secrets.DB_HOST,
  user=st.secrets.DB_USERNAME,
  password=st.secrets.DB_PASSWORD,
  port=3306,
  database=st.secrets["DB_NAME"],
  auth_plugin="mysql_native_password",
)

cur = conn.cursor(buffered=True)

try:
  id_escola = st.session_state["id_escola"]
except KeyError:
  st.error("Selecione uma escola a partir da Lista de Escolas")
  st.stop()


# turmas
cur.execute(f"""
select NO_TURMA as nome,
case when t.IN_DISC_QUIMICA = 1 then '✅' else '❌' end as química,
case when t.IN_DISC_FISICA = 1 then '✅' else '❌' end as física,
case when t.IN_DISC_MATEMATICA = 1 then '✅' else '❌' end as matemática,
case when t.IN_DISC_BIOLOGIA = 1 then '✅' else '❌' end as biologia,
case when t.IN_DISC_CIENCIAS = 1 then '✅' else '❌' end as ciências,
case when t.IN_DISC_LINGUA_PORTUGUESA = 1 then '✅' else '❌' end as português,
case when t.IN_DISC_LINGUA_INGLES = 1 then '✅' else '❌' end as inglês,
case when t.IN_DISC_LINGUA_ESPANHOL = 1 then '✅' else '❌' end as espanhol,
case when t.IN_DISC_LINGUA_FRANCES = 1 then '✅' else '❌' end as francês,
case when t.IN_DISC_LINGUA_OUTRA = 1 then '✅' else '❌' end as outra_língua,
case when t.IN_DISC_LINGUA_INDIGENA = 1 then '✅' else '❌' end as língua_indígena,
case when t.IN_DISC_ARTES = 1 then '✅' else '❌' end as artes,
case when t.IN_DISC_EDUCACAO_FISICA = 1 then '✅' else '❌' end as ed_física,
case when t.IN_DISC_HISTORIA = 1 then '✅' else '❌' end as história,
case when t.IN_DISC_GEOGRAFIA = 1 then '✅' else '❌' end as geografia,
case when t.IN_DISC_FILOSOFIA = 1 then '✅' else '❌' end as filosofia,
case when t.IN_DISC_ENSINO_RELIGIOSO = 1 then '✅' else '❌' end as ensino_religioso,
case when t.IN_DISC_ESTUDOS_SOCIAIS = 1 then '✅' else '❌' end as estudos_sociais,
case when t.IN_DISC_SOCIOLOGIA = 1 then '✅' else '❌' end as sociologia,
case when t.IN_DISC_EST_SOCIAIS_SOCIOLOGIA = 1 then '✅' else '❌' end as estudos_sociais_ou_sociologia,
case when t.IN_DISC_INFORMATICA_COMPUTACAO = 1 then '✅' else '❌' end as informática_computação,
case when t.IN_DISC_PROFISSIONALIZANTE = 1 then '✅' else '❌' end as disciplinas_profissionalizantes,
case when t.IN_DISC_ATENDIMENTO_ESPECIAIS = 1 then '✅' else '❌' end as atendimento_às_necessidades_educacionais_específicas,
case when t.IN_DISC_DIVER_SOCIO_CULTURAL = 1 then '✅' else '❌' end as diversidade_sociocultural,
case when t.IN_DISC_LIBRAS = 1 then '✅' else '❌' end as libras,
case when t.IN_DISC_PEDAGOGICAS = 1 then '✅' else '❌' end as disciplinas_pedagógicas,
case when t.IN_DISC_OUTRAS = 1 then '✅' else '❌' end as outras_disciplinas
from turma t where t.CO_ENTIDADE = {id_escola}""")
turmas = cur.fetchall()
df_turmas = pd.DataFrame(turmas, columns=cur.column_names)


## professores
cur.execute("""
select distinct d.CO_PESSOA_FISICA from escola e
  inner join docente d on d.CO_ENTIDADE = e.CO_ENTIDADE
  where e.CO_ENTIDADE = %s
""", (id_escola,))
docentes = cur.fetchall()
df_docentes = pd.DataFrame(docentes, columns=cur.column_names)


## alunos
cur.execute("""
select m.CO_PESSOA_FISICA from escola e
  inner join matricula m on m.CO_ENTIDADE = e.CO_ENTIDADE
  where e.CO_ENTIDADE = %s
""", (id_escola,))
alunos = cur.fetchall()
df_alunos = pd.DataFrame(alunos, columns=cur.column_names)

# exibir nome e dados
cur.execute(f"SELECT NO_ENTIDADE as nome FROM escola e WHERE e.CO_ENTIDADE = {id_escola}")
escola = cur.fetchone()
df = pd.DataFrame([escola], columns=cur.column_names)
escola = df.to_dict(orient="records")[0]
st.header(f"{escola['nome']} `{id_escola}`")
st.write(f"### `{len(df_turmas)}` turmas, `{len(df_docentes)}` docentes, `{len(df_alunos)}` alunos")

def is_bookmarked(id_escola):
  cur.execute("SELECT * FROM bookmark WHERE id_entidade = %s and id_usuario = %s", (id_escola, st.session_state['user_id']))
  return cur.fetchone() is not None

def add_bookmark(id_escola):  
  cursor = conn.cursor()
  try:
    cur.execute("INSERT INTO bookmark (id_entidade, id_usuario) VALUES (%s, %s)", (id_escola, st.session_state['user_id']))
    print("add bookmark", id_escola, st.session_state['user_id'])
  except Exception as e:
    print(e)
    conn.rollback()
    st.error(f"Erro ao adicionar bookmark")
  finally:
    cursor.close()
  conn.commit()

def remove_bookmark(id_escola):
  cursor = conn.cursor()
  try:
    cur.execute("DELETE FROM bookmark WHERE id_entidade = %s and id_usuario = %s", (id_escola, st.session_state['user_id']))
    print("remove bookmark", id_escola, st.session_state['user_id'])
  except Exception as e:
    print(e)
    conn.rollback()
    st.error(f"Erro ao remover bookmark")
  finally:
    cursor.close()
  conn.commit()

if "user_role" in st.session_state and st.session_state["user_role"] == "gerencial":
  if not is_bookmarked(id_escola):
    st.button("Adicionar Bookmark", key="bookmark", on_click=lambda: add_bookmark(id_escola))
  else:
    st.button("Remover Bookmark", key="unbookmark", on_click=lambda: remove_bookmark(id_escola))

st.write("## Turmas")
if "user_role" in st.session_state and st.session_state["user_role"] == "gerencial":
  st.download_button("Baixar turmas.csv", df_turmas.to_csv(), "turmas.csv", "text/csv")
AgGrid(df_turmas)

st.write("## Docentes")
st.write("Selecione um docente para ver detalhes")
if "user_role" in st.session_state and st.session_state["user_role"] == "gerencial":
  st.download_button("Baixar docentes.csv", df_docentes.to_csv(), "docentes.csv", "text/csv")
docente_gb = GridOptionsBuilder.from_dataframe(df_docentes)
docente_gb.configure_selection(selection_mode="single")
docente_gb.configure_side_bar()
gridOptions = docente_gb.build()

docente_data = AgGrid(
    df_docentes,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
)

docente_selected = docente_data["selected_rows"]

if docente_selected is not None and len(docente_selected) > 0:
    id_docente = docente_selected.values[0][0]
    st.write(f"### Docente `{id_docente}`")
    # buscar detalhes do docente
    cur.execute(f"""
    select d.CO_PESSOA_FISICA as id,
    d.NU_IDADE as idade,
    NU_DIA as dia_nascimento,
    NU_MES as mes_nascimento,
    NU_ANO as ano_nascimento,
    d.TP_SEXO as sexo,
    d.TP_COR_RACA as cor,
    d.TP_NACIONALIDADE as nacionalidade
    from docente d where d.CO_PESSOA_FISICA = {id_docente}
    """)
    docente = cur.fetchone()
    df_docente = pd.DataFrame([docente], columns=cur.column_names)
    AgGrid(df_docente)


st.write("## Alunos")
st.write("Selecione um aluno para ver detalhes")
if "user_role" in st.session_state and st.session_state["user_role"] == "gerencial":
  st.download_button("Baixar alunos.csv", df_alunos.to_csv(), "alunos.csv", "text/csv")
aluno_gb = GridOptionsBuilder.from_dataframe(df_alunos)
aluno_gb.configure_selection(selection_mode="single")
aluno_gb.configure_side_bar()
gridOptions = aluno_gb.build()

aluno_data = AgGrid(
    df_alunos,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
)

aluno_selected = aluno_data["selected_rows"]

if aluno_selected is not None and len(aluno_selected) > 0:
    id_aluno = aluno_selected.values[0][0]
    st.write(f"### Aluno `{id_aluno}`")
    # buscar detalhes do aluno
    cur.execute(f"""
    select d.CO_PESSOA_FISICA as id,
    d.NU_IDADE as idade,
    NU_DIA as dia_nascimento,
    NU_MES as mes_nascimento,
    NU_ANO as ano_nascimento,
    d.TP_SEXO as sexo,
    d.TP_COR_RACA as cor,
    d.TP_NACIONALIDADE as nacionalidade
    from matricula d where d.CO_PESSOA_FISICA = {id_aluno}
    """)
    aluno = cur.fetchone()
    df_aluno = pd.DataFrame([aluno], columns=cur.column_names)
    AgGrid(df_aluno)
