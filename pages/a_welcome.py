import streamlit as st
import extras.session_manager as sessions

# session update and state change 

sessions.update()
st.session_state['state_machine'].send("reset")


# page content

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


st.page_link("pages/b_mark.py", label="Start", use_container_width=True, icon="👍")

# debug stuff

# if st.button("Show state machine state"):
#     sessions.state_machine_dialog()
