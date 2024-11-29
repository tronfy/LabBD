import streamlit as st

st.set_page_config(
    layout="wide",
)

pages = []

if 'user_role' not in st.session_state:
  pages.append(st.Page("Login.py", title="Login", icon="👤"))
  pages.append(st.Page("Cadastro.py", title="Cadastro", icon="🔐"))
else:
  pages.append(st.Page("Escolas.py", title="Lista de Escolas", icon="🏫"))
  pages.append(st.Page("EscolaDetalhes.py", title="Detalhes de Escola", icon="📝"))

  if st.session_state['user_role'] == "gerencial":
    pages.append(st.Page("Bookmarks.py", title="Minhas Bookmarks", icon="🔖"))
    pages.append(st.Page("Usuarios.py", title="Lista de Usuários", icon="👥"))

  pages.append(st.Page("Logout.py", title="Logout", icon="↪️"))

if 'user_name' in st.session_state:
  st.write(f"Olá, **{st.session_state['user_name']}**! Seu tipo de conta é **{st.session_state['user_role']}**.")
else:
  st.write("Olá! Faça login ou cadastre-se para continuar.")

pg = st.navigation(pages)
pg.run()
