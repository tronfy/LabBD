import streamlit as st


pages = []

# if 'user_role' not in st.session_state:
pages.append(st.Page("Login.py", title="Login"))
pages.append(st.Page("Cadastro.py", title="Cadastro"))
# else:
pages.append(st.Page("Logout.py", title="Logout"))

pages.append(st.Page("Escolas.py", title="Lista de Escolas"))
pages.append(st.Page("EscolaDetalhes.py", title="Detalhes de Escola"))
        

pg = st.navigation(pages)
pg.run()
