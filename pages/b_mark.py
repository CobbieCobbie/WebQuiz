import random
import streamlit as st
import extras.session_manager as sessions


@st.dialog("Description of the statement")
def choose(description):
   st.write(description)
   st.pills("Wahr oder Falsch?", [True, False], key=description)


# session update and state change 
sessions.update()
st.session_state['state_machine'].send("start")

st.header("Mark the true statements")

for s in st.session_state['statements']:
   if s.right_answer:
      if st.button(s.trueStatement):
         choose(s.description)
   else:
      if st.button(s.falseStatement):
         choose(s.description)


# from here only for MockUp purposes 

# statements = [
#             "Statement 1 Statement 1 Statement 1 Statement 1 Statement 1", 
#             "Statement 2 Statement 2 Statement 2 Statement 2 Statement 2", 
#             "Statement 3 Statement 3 Statement 3 Statement 3 Statement 3", 
#             "Statement 4 Statement 4 Statement 4 Statement 4 Statement 4", 
#             "Statement 5 Statement 5 Statement 5 Statement 5 Statement 5"
#             ]

# st.pills("Statements", statements, selection_mode="multi")

# st.write("st.pills environment is not suitable for long text in the description")


# for s in st.session_state['statements']:

# if st.session_state['statement_evaluation'] != {}:
#    for key, value in st.session_state['statement_evaluation'].items():
#       if st.button(key):
#          st.write(key)

#    if coin:
#       st.session_state['statement_evaluation'][s.trueStatement] = True
#       if st.button(s.trueStatement):
#          choose(s.description)
   

#    else:
#       st.session_state['statement_evaluation'][s.falseStatement] = True
#       if st.button(s.falseStatement):
#          choose(s.description)

st.page_link("pages/c_evaluation.py", label="Evaluate", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sesions.state_machine_dialog()
