import streamlit as st
import extras.session_manager as sessions


st.session_state['state_machine'].send("eval")
sessions.update()

st.header("Evaluation of your marked statements")


st.page_link("pages/d_end.py", label="Finish Quiz", use_container_width=True, icon="👍")


# debug stuff

# @st.dialog("State of the state machine")
# def state_machine_dialog():
#     st.write("The state machine is currently in state "+ st.session_state['state_machine'].current_state.id)
#     if st.button("Close the dialog"):
#         st.rerun()
# if st.button("show state"):
#     state_machine_dialog()

