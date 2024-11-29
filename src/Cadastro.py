import streamlit as st
import mysql.connector
import datetime

conn = mysql.connector.connect(
    host=st.secrets.DB_HOST,
    user=st.secrets.DB_USERNAME,
    password=st.secrets.DB_PASSWORD,
    port=3306,
    database=st.secrets["DB_NAME"],
    auth_plugin="mysql_native_password",
)


def validar(nome, email, senha, dt_nasc):
    if nome == "" or email == "" or senha == "" or dt_nasc == "":
        return False
    return True


def cadastra_usuario(nome, email, senha, dt_nasc, gerencial=False):
    cursor = conn.cursor()
    success = False
    try:
        cursor.execute(
            "INSERT INTO usuario (nome, email, senha, data_nascimento, gerencial) VALUES (%s, %s, %s, %s, %s)",
            (nome, email, senha, dt_nasc, gerencial),
        )
        success = True
    except Exception as e:
        conn.rollback()
        st.error(f"Erro ao cadastrar o usuário {e}")
    finally:
        cursor.close()
    conn.commit()

    if success:
        st.success("Usuário cadastrado.")
        st.switch_page("Login.py")


with st.form("cadastro"):
    st.title("Cadastro de usuários")
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:", type="password")
    gerencial = st.checkbox("Gerencial")
    dt_nasc = st.date_input(
        "Data de nascimento:",
        min_value=datetime.date(1924, 1, 1),
        max_value=datetime.date(2024, 1, 1),
        format="DD/MM/YYYY",
    )
    submit = st.form_submit_button("Enviar")

if submit and validar(nome, email, senha, dt_nasc):
    # se o form for submetido e os dados estiverem válidos
    cadastra_usuario(nome, email, senha, dt_nasc, gerencial)
elif submit:
    # se o form for submetido mas com dados inválidos
    st.warning("Dados inválidos")
