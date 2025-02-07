import streamlit as st
import extras.session_manager as sessions

@st.dialog("Your choice")
def evaluate(boolean, description):
   st.write("This is ", boolean)   
   st.write(description)


# session update and state change 
sessions.update()
st.session_state['state_machine'].send("eval")

st.header("Evaluation of your marked statements")

for s in st.session_state['statements']:
    if s.right_answer:
        if st.button(s.trueStatement):
            evaluate(True, s.description)
    else:
        if st.button(s.falseStatement):
            evaluate(False, s.description)
# st.markdown("")
# st.button("Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2")
# st.markdown("")
# st.button("Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3")
# st.markdown("")
# st.button("Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4")
# st.markdown("")
# st.button("Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5")



st.page_link("pages/d_end.py", label="Finish Quiz", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sessions.state_machine_dialog()
