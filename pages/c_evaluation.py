import streamlit as st
import extras.session_manager as sessions

@st.dialog("Your choice")
def evaluate(boolean):
   st.write("You have chosen: ", boolean)   
   st.write("Based on the fact that ....")

sessions.update()
st.session_state['state_machine'].send("eval")

st.header("Evaluation of your marked statements")

if st.button("Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1"):
    evaluate(True)
if st.button("Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2"):
    evaluate(False)

if st.button("Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3"):
    evaluate(True)

if st.button("Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4"):
    evaluate(False)

if st.button("Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5"):
    evaluate(True)
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
