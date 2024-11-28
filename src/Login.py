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


def validar(email, senha):
    if not email or "@" not in email:
        st.warning("Email inválido")
        return False
    if not senha:
        st.warning("Insira sua senha")
        return False
    return True


def login_usuario(email, senha):
    cursor = conn.cursor()
    print(senha)
    cursor.execute(
        "SELECT * FROM usuario WHERE email=%s AND senha=%s", (email, senha)
    )
    usuario = cursor.fetchone()
    if usuario:
        return True
    else:
        return False


with st.form("login"):
    st.title("Login")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:", type="password")
    submit = st.form_submit_button("Entrar")

if submit and validar(email, senha):
    # se o form for submetido e os dados estiverem válidos
    if login_usuario(email, senha):
        st.success("Login efetuado com sucesso")
    else:
        st.warning("Usuário ou senha inválidos")