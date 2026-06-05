import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.resume_analyzer import analyze_resume_strength
from utils.theme import load_theme

load_theme()

st.title(
    "📄 Resume Strength Analyzer"
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    result = analyze_resume_strength(
        resume_text
    )

    st.subheader(
        "Resume Quality Score"
    )

    st.progress(
        result["score"]/100
    )

    st.metric(
        "Score",
        result["score"]
    )

    c1,c2 = st.columns(2)

    with c1:

        st.subheader(
            "✅ Strengths"
        )

        for item in result["strengths"]:

            st.success(item)

    with c2:

        st.subheader(
            "❌ Weaknesses"
        )

        for item in result["weaknesses"]:

            st.error(item)

    st.subheader(
        "💡 Suggestions"
    )

    for item in result["suggestions"]:

        st.info(item)

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

# st.sidebar.info(
#     f"👤 {email}"
# )