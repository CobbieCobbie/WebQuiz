import streamlit as st
from streamlit_javascript import st_javascript
import Quiz.state_machine as sm


def init():
    if 'state_machine' not in st.session_state:
        st.session_state['state_machine'] = sm.QuizStateMachine(allow_event_without_transition=True)
    
    if 'statements' not in st.session_state:
        st.session_state['statements'] = [
            "Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 Statement 1 ", 
            "Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 Statement 2 ", 
            "Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 Statement 3 ", 
            "Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 Statement 4 ", 
            "Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 Statement 5 "
            ]

def update():
    if 'state_machine' not in st.session_state:
        init()
        
        
# static methods

@staticmethod
def get_multipage():
    url = st_javascript("await fetch('').then(r => window.parent.location.href)")
    return url

