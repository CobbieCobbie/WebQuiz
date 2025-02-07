import streamlit as st
from streamlit_extras.stylable_container import stylable_container


with stylable_container(key="my_unique_button",css_styles="""
{
    [data-testid="baseButton-secondary"] {
        background-color: red;
    }
}
""",):
    st.button("my colored button")
