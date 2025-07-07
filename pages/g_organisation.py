import random
import streamlit as st
import extras.session_manager as sessions

from modules.reifegrad import load_questions_from_json

# Lade die Fragen
data = load_questions_from_json('data/6_organisations_und_unternehmenskultur.json')

# SessionState initialisieren für dieses Topic
if 'answers_management' not in st.session_state:
    st.session_state['answers_management'] = {}

# Überschrift
st.title(data['topic'])

# Fragen anzeigen
for q in data['questions']:
    answer = st.radio(
        q['question'],
        q['options'],
        key=f"management_{q['id']}"
    )
    # Speichere Antwort in SessionState
    st.session_state['answers_management'][q['id']] = answer

# Optional: Debug-Ausgabe
st.write("Aktuelle Antworten:", st.session_state['answers_management'])

# Speichern Button (z.B. in DB oder Datei)
if st.button("Antworten speichern"):
    # Hier kannst du deine Logik für Speicherung einfügen
    st.success("Antworten wurden gespeichert.")
st.page_link("pages/h_evaluation.py", label="Evaluate", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sesions.state_machine_dialog()
