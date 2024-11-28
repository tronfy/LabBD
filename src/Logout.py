import streamlit as st

st.session_state.pop("user_name", None)
st.session_state.pop("user_role", None)
st.rerun()
