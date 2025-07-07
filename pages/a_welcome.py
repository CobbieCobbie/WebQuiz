import streamlit as st
import extras.session_manager as sessions

# session update and state change 

sessions.update()
st.session_state['state_machine'].send("reset")


# page content

st.title("Willkommen zur interaktiven Reifegradanalyse")


st.markdown(
"""
# Dies ist die interaktive Reifegradanalyse

## Mehrere Themengebiete werden abgefragt
Die Reifegradanalyse besteht aus mehreren Themengebieten, die jeweils mehrere Aussagen enthalten.

Beurteilen sie die Aussagen wahrheitsgemäß mit "Ja" oder "Nein".
"""
)


st.page_link("pages/b_management.py", label="Start", use_container_width=True, icon="👍")

# debug stuff

# if st.button("Show state machine state"):
#     sessions.state_machine_dialog()
