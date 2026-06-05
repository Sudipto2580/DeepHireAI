import streamlit as st

def load_theme():

    theme = st.session_state.get(
        "theme",
        "Dark"
    )

    theme_map = {
        "Dark":"assets/styles.css",
        "Light":"assets/light.css",
        "Midnight":"assets/midnight.css",
        "Corporate":"assets/corporate.css"
    }

    css_file = theme_map.get(
        theme,
        "assets/styles.css"
    )

    with open(css_file) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )