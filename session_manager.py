import streamlit as st
import Quiz.state_machine as sm


def init():
    if 'state_machine' not in st.session_state:
        st.session_state['state_machine'] = sm.QuizStateMachine(allow_event_without_transition=True)

