import streamlit as st
from streamlit_star_rating import st_star_rating

import extras.session_manager as sessions


sessions.update()
st.session_state['state_machine'].send("end")

st.header("That's it! You have finished the quiz.")

max_statements = 5
correct_statements = 5

if correct_statements == max_statements:
    st.balloons()
    st.toast("Good job!", icon="🎈")

st_star_rating(label = None, maxValue = max_statements, defaultValue = correct_statements, key = "rating", read_only = True)

st.page_link("pages/a_welcome.py", label="Restart", use_container_width=True, icon="👍")



# debug stuff

if st.button("Show state machine state"):
    sessions.state_machine_dialog()

# if correct_statements == 0:
#     st.toast("You suck!", icon="👎")

