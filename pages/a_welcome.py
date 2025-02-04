import streamlit as st
import session_manager as sessions


st.session_state['state_machine'].send("reset")

st.title("Welcome to the Quiz")


st.markdown(
"""
# This is the Welcome Screen

## Demonstration of your choice
Place some information about your demonstration here

## How to play
Click on the statements that you think that are true. When you are done, press the button "Evaluate". Enjoy!           
"""
)



@st.dialog("State of the state machine")
def state_machine_dialog():
    st.write("The state machine is currently in state "+ st.session_state['state_machine'].current_state.id)
    if st.button("Close the dialog"):
        st.rerun()

if st.button("show state"):
    state_machine_dialog()


st.page_link("pages/b_mark.py", label="Start", use_container_width=True, icon="👍")
