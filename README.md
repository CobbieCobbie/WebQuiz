# Quiz Web App Template

Welcome to the README of the Web Quiz Web App Template! This project is a streamlit multi-page implementation of a quiz. 

## Content

This is a multi-page streamlit application. In extras/, the session_manager uses the state machine to keep the session going. Questions are loaded via JSON and de-serialized (Quiz/) to be loaded into a session. Almost everything is a st.session_state here. 

## How to install

You have to have a running python system. I recommend initializing a virtual python environment, I used python 3.12 (venv) but I guess every python >= 3.10 will be fine. If not, please let me know.

Install the dependencies

```
pip install -r requirements.txt
```

This will *streamlit* and *statemachine* modules, also *streamlit-js* and *st-star-rating*. The versions in the requirements.txt are those I used.

To start this all, run
```
streamlit run ./quiz.py --client.showSidebarNavigation false --browser.gatherUsageStats=false
```

This will set up a local web server and open a client in your default browser.

Since we work with streamlits [st.page_link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link), iterating over all pages, we can disable the sidebar for the pages. Also, we will run streamlit without Streamlit stats gathering. That's what the args are for

## streamlit configuration

u can call 
```
streamlit config show
```
to see the current configuration of your localhost / server. If you want to e.g. disable global side-bar navigation, certain warnings, set the server port or alter the colors for every client and so on, please have a look [here](https://docs.streamlit.io/develop/api-reference/configuration/config.toml).

## vscode config

For debugging, include the `launch.json` into your `.vscode` directory of the project
