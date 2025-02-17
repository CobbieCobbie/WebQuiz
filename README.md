# Quiz Web App Template

Welcome to the README of the Web Quiz Web App Template! In this  

## Content

## How to install

You have to have a running python system. I recommend initializing a virtual python environment.

Install the dependencies

```
pip install -r requirements.txt
```

This will install *streamlit* and *statemachine* modules.

Since we work with streamlits [st.page_link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link), we can disable the sidebar for the pages

To do this, run
```
streamlit run ./quiz_test.py --client.showSidebarNavigation false --browser.gatherUsageStats=false
```

This will set up a local web server and open a client in your default browser.

## streamlit configuration

u can call 
```
streamlit config show
```
to see the current configuration

## vscode config

For debugging, include the `launch.json` into your `.vscode` directory of the project