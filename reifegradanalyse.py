import streamlit as st
import extras.session_manager as sessions


sessions.init()

st.title("Interaktive Reifegradanalyse")
st.write("Dies ist eine interaktive Reifegradanalyse.")

st.page_link("pages/a_welcome.py", label="Initialisierung", use_container_width=True, icon="👍")
