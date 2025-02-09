import streamlit as st
import extras.session_manager as sessions

@st.dialog("Your choice")
def evaluate(statement):
   st.write("This is ", statement.rightAnswer)   
   st.write(statement.description)


# session update and state change 
sessions.update()
st.session_state['state_machine'].send("eval")

st.header("Evaluation of your marked statements")

for s in st.session_state['statements']:
    if st.button(s.chosenStatement):
        evaluate(s)

st.page_link("pages/d_end.py", label="Finish Quiz", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sessions.state_machine_dialog()
