import streamlit as st
import extras.session_manager as sessions


@st.dialog("Description of the statement")
def choose(description):
   st.write("The description is: ", description)
   st.pills("Evaluation", [True, False], key=description)

sessions.update()
st.session_state['state_machine'].send("start")

st.header("Mark the true statements")

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

if st.button("Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1"):
   choose("Description 1")
if st.button("Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2"):
   choose("Description 2")

if st.button("Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3"):
   choose("Description 3")

if st.button("Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4"):
   choose("Description 4")

if st.button("Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5"):
   choose("Description 5")


st.write("st.button are suited to carry long descriptions")


st.page_link("pages/c_evaluation.py", label="Evaluate", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sesions.state_machine_dialog()
