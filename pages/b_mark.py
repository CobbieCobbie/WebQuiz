import streamlit as st
import extras.session_manager as sessions


st.session_state['state_machine'].send("start")
sessions.update()

st.header("Mark the true statements")

# WIP

statements = [
            "Statement 1 Statement 1 Statement 1 Statement 1 Statement 1", 
            "Statement 2 Statement 2 Statement 2 Statement 2 Statement 2", 
            "Statement 3 Statement 3 Statement 3 Statement 3 Statement 3", 
            "Statement 4 Statement 4 Statement 4 Statement 4 Statement 4", 
            "Statement 5 Statement 5 Statement 5 Statement 5 Statement 5"
            ]

st.pills("Statements", statements, selection_mode="multi")


st.page_link("pages/c_evaluation.py", label="Evaluate", use_container_width=True, icon="👍")



# debug stuff

@st.dialog("State of the state machine")
def state_machine_dialog():
    st.write("The state machine is currently in state "+ st.session_state['state_machine'].current_state.id)
if st.button("Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 "):
     state_machine_dialog()

