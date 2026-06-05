import streamlit as st

from utils.llm import ask_llm
from utils.theme import load_theme

load_theme()

st.title(
    "🤖 AI Recruiter"
)

question = st.text_area(
    "Ask Recruiter AI"
)

if st.button(
    "Ask"
):

    answer = ask_llm(
        question
    )

    st.write(answer)

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

# st.sidebar.info(
#     f"👤 {email}"
# )