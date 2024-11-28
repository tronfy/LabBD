import streamlit as st


pages = []

if 'user_role' not in st.session_state:
  pages.append(st.Page("Login.py", title="Login"))
  pages.append(st.Page("Cadastro.py", title="Cadastro"))
else:
  pages.append(st.Page("Escolas.py", title="Lista de Escolas"))
  pages.append(st.Page("EscolaDetalhes.py", title="Detalhes de Escola"))

  pages.append(st.Page("Logout.py", title="Logout"))

if 'user_name' in st.session_state:
  st.write(f"Olá, **{st.session_state['user_name']}**! Seu tipo de conta é **{st.session_state['user_role']}**.")

pg = st.navigation(pages)
pg.run()
