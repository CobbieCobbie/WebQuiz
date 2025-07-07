import streamlit as st
import extras.session_manager as sessions

from streamlit_star_rating import st_star_rating
from collections import defaultdict


# session update and state change 
sessions.update()
st.session_state['state_machine'].send("eval")

st.header("Evaluation der Antworten")

def get_category_stats(answers_management):
    stats = defaultdict(lambda: {"total": 0, "ja": 0})
    for key, value in answers_management.items():
        if "." in key:
            category, qid = key.split(".", 1)
            stats[category]["total"] += 1
            if value == "Ja":
                stats[category]["ja"] += 1
    return stats

if "answers_management" in st.session_state:
    stats = get_category_stats(st.session_state["answers_management"])
    st.subheader("Kategorie-Auswertung")
    for category, data in stats.items():
        st_star_rating(
            label=None,
            maxValue=data["total"],
            defaultValue=data["ja"],
            key=f"rating_{category}",
            read_only=True
        )
        st.write(f"Kategorie **{category}**: {data['ja']} von {data['total']} Antworten mit 'Ja'")

st.markdown("""
            Haben Sie in einem Bereich kein- bis einmal die Antwortoption „Ja“ ausgewählt, besteht hier ein großes Entwicklungspotenzial. Es existieren teilweise bereits benötigte Prozesse und Strukturen, aber an der um-fänglichen Umsetzung und Implementierung scheitert es bisher. Hier sollten Sie ein besonderes Augenmerk drauf lenken und Verbesserungspotenziale erarbeiten.

            Haben Sie in einem Bereich einige Antwortoption „Ja“ ausgewählt, haben Sie bereits (Groß-)Teile der Prozesse und der benötigten Strukturen etabliert oder umgesetzt. Allerdings bestehen an verschiedenen Stellen noch viele Ausbaumöglichkeiten und Entwicklungspotenziale. Mithilfe der eben durchgeführten Reife-gradanalyse wissen Sie nun in welchen Bereichen ihre Potenziale und auch ihre Schwachstellen liegen.

            Wenn Sie in einem Bereich (annähernd) alle Antwortoption „Ja“ ausgewählt haben, haben Sie bereits ef-fektive Prozesse und Strukturen etabliert, die einer regelmäßigen Effektivitätsüberprüfung unterliegen und dadurch kontinuierlich verbessert werden. In diesem Themengebiet haben Sie (fast) alle Schwachstellen er-kannt und befinden sich auf einem (sehr) guten Niveau. Aber dennoch gibt es stets Weiterentwicklungspo-tential!            
            """)
        

"Management von Projekten"
# st_star_rating(label = None, maxValue = stats, defaultValue = correct_statements, key = "rating", read_only = True)


st.page_link("pages/i_end.py", label="Finish Quiz", use_container_width=True, icon="👍")


# methods


# debug stuff

# if st.button("Show state machine state"):
#     sessions.state_machine_dialog()
