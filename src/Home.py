import streamlit as st

pg = st.navigation([
    st.Page("nav/Login.py"),
    st.Page("nav/Cadastro.py"),
    st.Page("nav/Escolas.py", title="Lista de Escolas"),
    st.Page("nav/EscolaDetalhes.py", title="Detalhes de Escola"),
], position="sidebar")

pg.run()