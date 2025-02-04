import streamlit as st

st.header("Thanks for playing!")


st.session_state['state_machine'].send("cycle")

@st.dialog("State of the state machine")
def state_machine_dialog():
    st.write("The state machine is currently in state "+ st.session_state['state_machine'].current_state.id)
    if st.button("Close the dialog"):
        st.rerun()

if st.button("show state"):
    state_machine_dialog()


st.page_link("pages/a_welcome.py", label="Restart", use_container_width=True, icon="👍")
