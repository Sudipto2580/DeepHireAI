import streamlit as st

from utils.pdf_parser import (
    extract_text_from_pdf
)

from utils.resume_chat import (
    ask_resume_question
)
from utils.theme import load_theme

load_theme()

st.title(
    "🤖 Resume AI Assistant"
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    st.success(
        "Resume Loaded"
    )

    question = st.text_input(
        "Ask about the candidate"
    )

    if st.button(
        "Ask AI"
    ):

        answer = ask_resume_question(
            resume_text,
            question
        )

        st.markdown(
            "### AI Response"
        )

        st.write(
            answer
        )

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

# st.sidebar.info(
#     f"👤 {email}"
# )