import streamlit as st
from streamlit_star_rating import st_star_rating

import extras.session_manager as sessions

# session update and state change 

sessions.update()
st.session_state['state_machine'].send("end")

# page content

st.header("Danke für das Ausfüllen!")

st.balloons()
st.toast("Geschafft!", icon="🎈")

st.markdown("""
            Herzlichen Dank, dass Sie unsere Reifegradanalyse durchgeführt haben! Sie haben damit einen wichtigen Schritt in Richtung kontinuierlicher Verbesserung und strategischer Weiterentwicklung Ihres Unternehmens unternommen. Die gewonnenen Erkenntnisse sind der Schlüssel, um gezielte Maßnahmen zur Optimierung zu planen und Ihre Ziele erfolgreich zu erreichen.

            Nutzen Sie die Ergebnisse Ihrer Reifegradanalyse, um konkret und zielgerichtet ihre unternehmerischen Schwachstellen zu identifizieren und Ihre Potentiale zu heben. Das Projektteam ist gerne für Sie da!

            Sollten Sie Fragen zu den Ergebnissen oder zur Umsetzung der nächsten Schritte haben, zögern Sie bitte nicht uns zu kontaktieren. Unser Team steht Ihnen jederzeit zur Verfügung, um Sie mit Rat und Tat zu unterstützen. Gemeinsam können wir daran arbeiten, Ihr Unternehmen bei der Weiterentwicklung voranzubringen.
            """)

st.page_link("pages/a_welcome.py", label="Restart", use_container_width=True, icon="👍")


# debug stuff

# if st.button("Show state machine state"):
#     sessions.state_machine_dialog()

# if correct_statements == 0:
#     st.toast("You suck!", icon="👎")
