import streamlit as st

import pandas as pd
import plotly.graph_objects as go

from utils.pdf_parser import extract_text_from_pdf
from utils.candidate_processor import process_candidate
from utils.supabase_db import insert_candidate
from utils.ranking import rank_candidates
from utils.report_generator import create_report
from utils.recommendation import (
    get_recommendation,
    hiring_probability
)
from utils.theme import load_theme

load_theme()

# -----------------------------
# AUTH CHECK
# -----------------------------

if not st.session_state.get(
    "logged_in",
    False
):
    st.switch_page("app.py")

# -----------------------------
# THEME
# -----------------------------

css_file = (
    "assets/styles.css"
    if st.session_state.get(
        "theme",
        "Dark"
    ) == "Dark"
    else "assets/light.css"
)

with open(css_file) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.markdown("""
# 🤖 DeepHire AI
""")

st.sidebar.success(
    f"👤 {st.session_state.user_email}"
)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div style="
padding:30px;
border-radius:25px;
background:
linear-gradient(
90deg,
#2563EB,
#7C3AED
);
margin-bottom:25px;
">

<h1 style="color:white;">
📄 ATS Analysis
</h1>

<p style="color:white;">
Enterprise Resume Intelligence Engine
</p>

</div>
""",
unsafe_allow_html=True)

st.caption(
    "Transformer Powered Resume Screening"
)

# -----------------------------
# INPUTS
# -----------------------------

job_description = st.text_area(
    "Paste Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Candidate Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# -----------------------------
# RECOMMENDATION
# -----------------------------

def get_recommendation(score):

    if score >= 80:
        return "🟢 Strong Match"

    elif score >= 60:
        return "🟡 Manual Review"

    return "🔴 Not Recommended"

# -----------------------------
# ANALYSIS
# -----------------------------

if st.button(
    "Analyze Candidates"
):

    if not uploaded_files:

        st.warning(
            "Upload resumes first"
        )

    elif not job_description:

        st.warning(
            "Enter Job Description"
        )

    else:

        candidates = []

        with st.spinner(
            "Analyzing resumes..."
        ):

            for file in uploaded_files:

                resume_text = extract_text_from_pdf(
                    file
                )
                
                result = process_candidate(
                    resume_text,
                    job_description
                )
               
                candidate = {

                    "user_email":
                    st.session_state.user_email,

                    "filename":
                    file.name,

                    "score":
                    result["final_score"],

                    "semantic":
                    result["semantic_score"],

                    "skill":
                    result["skill_score"],

                    "tfidf":
                    result["tfidf_score"],

                    "matched":
                    ", ".join(
                        result["matched_skills"]
                    ),

                    "missing":
                    ", ".join(
                        result["missing_skills"]
                    ),

                    "recommendation":
                    get_recommendation(
                        result["final_score"]
                    )

                }

                candidates.append(
                    candidate
                )

                insert_candidate(
                    candidate
                )

        ranked = rank_candidates(
            candidates
        )

        df = pd.DataFrame(
            ranked
        )

        st.success(
            "Analysis Complete"
        )

        # -------------------------
        # TOP CANDIDATE
        # -------------------------

        top = ranked[0]

        st.subheader(
            "🏆 Top Candidate"
        )

        c1,c2,c3,c4 = st.columns(4)

        c1.metric(
            "ATS Score",
            top["score"]
        )

        c2.metric(
            "Semantic Match",
            top["semantic"]
        )

        c3.metric(
            "Skill Match",
            top["skill"]
        )

        c4.metric(
            "TF-IDF Match",
            top["tfidf"]
        )

        st.info(
            f"Recommendation: {top['recommendation']}"
        )

        # -------------------------
        # ATS GAUGE
        # -------------------------

        fig = go.Figure(
        go.Indicator(
        mode="gauge+number",
        value=top["score"],
        title={"text":"ATS Score"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"#38BDF8"},
            "bgcolor":"#111827"
             }
            )
        )

        fig.update_layout(
            paper_bgcolor="#0B1220",
            font_color="white",
            height=350
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        # -------------------------
        # RANKING TABLE
        # -------------------------

        st.subheader(
            "📊 Candidate Ranking"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # -------------------------
        # CANDIDATE CARDS
        # -------------------------

        st.subheader(
            "👥 Candidate Insights"
        )

        for idx,row in df.iterrows():

            st.markdown(
                f"""
                <div style="
                background:#111827;
                padding:20px;
                border-radius:20px;
                margin-bottom:20px;
                border:1px solid #1E293B;
                ">

                <h3>#{idx+1} {row['filename']}</h3>

                <p><b>ATS Score:</b> {row['score']}</p>

                <p><b>Recommendation:</b> {row['recommendation']}</p>

                <p><b>Matched Skills:</b> {row['matched']}</p>

                <p><b>Missing Skills:</b> {row['missing']}</p>

                <p><b>TF-IDF Match:</b> {row['tfidf']}</p>

                </div>
                """,
                unsafe_allow_html=True
                )
            
            st.success("Matched Skills")
            st.error("Missing Skills")
            # compute per-candidate hiring probability
            probability = hiring_probability(row['score'])
            st.metric("Hiring Probability", f"{probability}%")

            st.divider()

        # -------------------------
        # EXPORTS
        # -------------------------

        st.subheader(
            "📥 Export Results"
        )

        st.download_button(
            "Download CSV",
            data=df.to_csv(
                index=False
            ),
            file_name=
            "candidate_ranking.csv"
        )

        report_path = create_report(
            df
        )

        with open(
            report_path,
            "rb"
        ) as pdf:

            st.download_button(
                "Download PDF Report",
                pdf,
                file_name=
                "DeepHire_Report.pdf"
            )

        st.markdown("### 📌 Recommendation")

        recommendation = get_recommendation(
            result["final_score"]
        )

        probability = hiring_probability(
            result["final_score"]
        )

        st.success(
            f"{recommendation}"
        )

        st.info(
            f"Hiring Probability: {probability}%"
        )
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Strengths")
            if result["matched_skills"]:
                for skill in result["matched_skills"]:
                    st.write(f"✔ {skill}")

        with col2:
            st.subheader("❌ Missing Skills")
            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.write(f"✘ {skill}") 

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

# st.sidebar.info(
#     f"👤 {email}"
# )