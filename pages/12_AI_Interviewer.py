import streamlit as st
from utils.interview_agent import (
    generate_interview_questions,
    evaluate_candidate
)
from utils.theme import load_theme

load_theme()

st.set_page_config(
    page_title="AI Interview Agent",
    layout="wide"
)

st.title(
    "🎤 DeepHire AI Interview Agent"
)

st.caption(
    "LLM Powered Candidate Evaluation"
)

job_role = st.text_input(
    "Job Role",
    value="Machine Learning Engineer"
)

skills = st.text_area(
    "Candidate Skills",
    value="Python, SQL, Machine Learning"
)

col1,col2 = st.columns(2)

with col1:

    if st.button(
        "Generate Interview Questions"
    ):

        questions = (
            generate_interview_questions(
                job_role,
                skills
            )
        )

        st.session_state[
            "questions"
        ] = questions

with col2:

    if st.button(
        "Clear Interview"
    ):

        st.session_state.clear()

if "questions" in st.session_state:

    st.subheader(
        "📋 Generated Questions"
    )

    st.info(
        st.session_state[
            "questions"
        ]
    )

    answers = st.text_area(
        "Candidate Answers",
        height=300
    )

    if st.button(
        "Evaluate Candidate"
    ):

        with st.spinner(
            "Evaluating..."
        ):

            evaluation = (
                evaluate_candidate(
                    st.session_state[
                        "questions"
                    ],
                    answers
                )
            )

        st.subheader(
            "📊 Interview Evaluation"
        )

        st.success(
            evaluation
        )

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

# st.sidebar.info(
#     f"👤 {email}"
# )