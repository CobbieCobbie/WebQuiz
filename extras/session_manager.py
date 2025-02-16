import random
import streamlit as st
from streamlit_javascript import st_javascript


import Quiz.state_machine as sm
import Quiz.Statement as Statement
import Quiz.QuizStatement as QuizStatement

def init():
    if 'state_machine' not in st.session_state:
        st.session_state['state_machine'] = sm.QuizStateMachine(allow_event_without_transition=True)
        
    if 'statement_amount' not in st.session_state:
        st.session_state['statement_amount'] = 5
    if 'statements' not in st.session_state:
        quiz_statements = []
        statements = Statement.Statement.load_from_file("Quiz/quiz_statements.json")        
        for s in statements:
            s = QuizStatement.QuizStatement(s.id, s.trueStatement, s.falseStatement, s.description)
            quiz_statements.append(s)
        while len(quiz_statements) > st.session_state['statement_amount']:
            quiz_statements.pop(random.randint(0, len(quiz_statements) - 1))
        st.session_state['statements'] = quiz_statements

    if 'right_answers' not in st.session_state:
        st.session_state['right_answers'] = 0


def update():
    if 'state_machine' not in st.session_state:
        init()
    elif 'statements' not in st.session_state:
        init()
    elif 'right_answers' not in st.session_state:
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

    if st.session_state['state_machine'].current_state == st.session_state['state_machine'].welcome:
        
        for s in st.session_state['statements']:
            coin = random.choice([True, False])
            s.rightAnswer = coin
            if coin:
                s.chosenStatement = s.trueStatement
            else:
                s.chosenStatement = s.falseStatement

# useful methods

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
