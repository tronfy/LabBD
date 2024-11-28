import streamlit as st

pg = st.navigation([
    st.Page("Login.py"),
    st.Page("Cadastro.py"),
    st.Page("Escolas.py", title="Lista de Escolas"),
    st.Page("EscolaDetalhes.py", title="Detalhes de Escola"),
], position="sidebar")

pg.run()
