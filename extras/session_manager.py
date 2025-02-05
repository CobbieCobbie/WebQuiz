import streamlit as st
from streamlit_javascript import st_javascript
import Quiz.state_machine as sm


def init():
    if 'state_machine' not in st.session_state:
        st.session_state['state_machine'] = sm.QuizStateMachine(allow_event_without_transition=True)
        
    if 'statements' not in st.session_state:
        st.session_state['statements'] = [
            "Statement 1", 
            "Statement 2", 
            "Statement 3", 
            "Statement 4", 
            "Statement 5"
            ]


def update():
    if 'state_machine' not in st.session_state:
        init()
    elif 'statements' not in st.session_state:
        init()
    page_name = get_multipage()
    match page_name:
        case "a_welcome":
            st.session_state['state_machine'].current_state = st.session_state['state_machine'].welcome
        case "b_mark":
            st.session_state['state_machine'].current_state = st.session_state['state_machine'].quiz_start
        case "c_evaluation":
            st.session_state['state_machine'].current_state = st.session_state['state_machine'].quiz_eval
        case "d_end":
            st.session_state['state_machine'].current_state = st.session_state['state_machine'].result
        case _:
            init()


# static methods

def get_multipage():
    url = st_javascript("await fetch('').then(r => window.parent.location.href)")
    result = url
    if isinstance(url, str):
        result = url.rsplit("/",1)[1]
    return result


@st.dialog("State of the state machine")
def state_machine_dialog():
    st.write("The state machine is currently in state \""+ st.session_state['state_machine'].current_state.id + "\"")
    if st.button("Close the dialog"):
        st.rerun()
