import streamlit as st
import extras.session_manager as sessions


sessions.init()

st.title("Quiz Web App Template")
st.write("This is a quiz testing page.")

st.page_link("pages/a_welcome.py", label="Initialize Quiz", use_container_width=True, icon="👍")
