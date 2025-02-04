import Quiz.Statement as Statement
import streamlit as st


st.title("Quiz Web App Template")
st.write("This is a quiz testing page.")

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()


st.page_link("pages/a_welcome.py", label="Initialize Quiz", use_container_width=True, icon="👍")

## For later use

# statements = Statement.Statement.load_from_file("Quiz/quiz_statements.json")

# @st.dialog("Streamlit Example Dialog")
# def example_dialog(some_arg: str, some_other_arg: int):
#     st.write(f"You passed following args: {some_arg} | {some_other_arg}")
#     # interacting with the text_input only re-runs `example_dialog`
#     some_text_input = st.text_input("Type something:", key="example_dialog_some_text_input")
#     # following write is updated when chaning the text_input inside the dialog
#     st.write(f"You wrote '{some_text_input}' in the dialog")
#     if st.button("Close the dialog"):
#         st.rerun()

# with st.popover("State"):
#     id = st.session_state['state_machine'].current_state.id
#     st.markdown(id)



# if st.button("Open dialog"):
#     example_dialog("Some string arg", 42)

# st.button("Cycle", on_click=lambda: st.write(st.session_state['state_machine'].send("cycle")))

# st.write(st.session_state['state_machine'].current_state.id)


# st.button("print test", on_click=lambda: st.write(st.session_state['test']))

# if st.button("alter test"):
#     st.session_state['test'] = "altered"
