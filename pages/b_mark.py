import random
import streamlit as st
import extras.session_manager as sessions


@st.dialog("Wahr oder falsch?")
def choose(statement):
   st.write(statement.description)
   statement.playerChoice = st.pills("Wahr oder Falsch?", [True, False], key=statement.description)


# session update and state change

sessions.update()
st.session_state['state_machine'].send("start")

st.header("Klick auf die Aussage und wähle wahr oder falsch")

for s in st.session_state['statements']:
   if st.button(s.chosenStatement, key=s.id):
      choose(s)

st.page_link("pages/c_evaluation.py", label="Evaluate", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sesions.state_machine_dialog()
