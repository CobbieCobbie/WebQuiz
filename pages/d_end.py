import streamlit as st
from streamlit_star_rating import st_star_rating

import extras.session_manager as sessions


st.session_state['state_machine'].send("end")
sessions.update()

st.header("Thanks for playing!")

max_statements = 5
correct_statements = 3

st_star_rating(label = None, maxValue = max_statements, defaultValue = correct_statements, key = "rating", read_only = True)

st.page_link("pages/a_welcome.py", label="Restart", use_container_width=True, icon="👍")



# debug stuff

# @st.dialog("State of the state machine")
# def state_machine_dialog():
#     st.write("The state machine is currently in state "+ st.session_state['state_machine'].current_state.id)
#     if st.button("Close the dialog"):
#         st.rerun()
# if st.button("show state"):
#     state_machine_dialog()

