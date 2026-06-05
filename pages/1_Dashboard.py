import streamlit as st
import pandas as pd
from utils.theme import load_theme

load_theme()
from utils.supabase_db import get_all_candidates

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

history = get_all_candidates()

if history:
    df = pd.DataFrame(history)
    df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
    ).fillna(0)
    total = len(df)
    
    df["score"] = pd.to_numeric(
        df["score"],
        errors="coerce"
    ).fillna(0)

    avg_score = round(
        df["score"].mean(),
        2
    )

    best_score = round(
        df["score"].max(),
        2
    )
else:
    df = pd.DataFrame(
        columns=[
            "iD",
            "filename",
            "score",
            "semantic",
            "skill",
            "matched",
            "missing",
        ]
    )
    total = 0
    avg_score = 0
    best_score = 0

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
text-align:center;
margin-bottom:20px;
">

<h1 style="
color:white;
font-size:60px;
">
🚀 DeepHire AI
</h1>

<p style="
color:white;
font-size:22px;
">
Enterprise Recruitment Intelligence Platform
</p>

</div>
""",
unsafe_allow_html=True)

strong_matches = len(
    df[df["score"] >= 80]
)


c1, c2, c3 ,c4 = st.columns(4)

c1.metric("👥 Candidates", total)

c2.metric(
    "📊 Average ATS",
    avg_score
)

c3.metric(
    "🏆 Best ATS",
    best_score
)

c4.metric(
    "⭐ Strong Matches",
    strong_matches
)


st.markdown("## 📈 Platform Overview")

left, right = st.columns([2, 1])

with left:
    st.markdown(
        """
        ### 🚀 AI Recruitment Engine

        DeepHire AI combines:

        - ATS Screening
        - Resume Intelligence
        - Gemini AI Assistant
        - AI Interview Agent
        - Candidate Analytics
        """
    )

with right:
    st.markdown(
        """
        ### 🧠 Models

        - Gemini 2.5 Flash
        - Sentence Transformer
        - TF-IDF
        - Cosine Similarity
        """
    )

    st.divider()

    st.subheader("📂 Recent Candidates")

if history:

    recent_df = (
        df[["filename", "score"]]
        .sort_values(
            by="score",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        recent_df,
        use_container_width=True
    )

else:
    st.info("No candidates yet.")

st.divider()

st.success("System Online")
email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

st.sidebar.info(
    f"👤 {email}"
)