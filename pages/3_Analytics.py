import streamlit as st

import pandas as pd
import plotly.express as px

from utils.supabase_db import get_all_candidates
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
# PAGE
# -----------------------------

st.title("📊 Recruitment Analytics")

history = get_all_candidates()

if not history:

    st.warning(
        "No candidate data available."
    )

    st.stop()

# -----------------------------
# DATAFRAME
# -----------------------------

df = pd.DataFrame(history)
df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
).fillna(0)

df["semantic"] = pd.to_numeric(
    df["semantic"],
    errors="coerce"
).fillna(0)

df["skill"] = pd.to_numeric(
    df["skill"],
    errors="coerce"
).fillna(0)

# -----------------------------
# KPI SECTION
# -----------------------------

st.subheader("📈 Recruitment Overview")

c1,c2,c3 = st.columns(3)

c1.metric(
    "Candidates",
    len(df)
)

c2.metric(
    "Average ATS",
    round(
        df["score"].mean(),
        2
    )
)

c3.metric(
    "Best ATS",
    round(
        df["score"].max(),
        2
    )
)

st.divider()

# -----------------------------
# ATS BAR CHART
# -----------------------------

st.subheader(
    "🏆 Candidate Ranking"
)

fig1 = px.bar(
    df.sort_values(
        by="score",
        ascending=False
    ),
    x="filename",
    y="score",
    color="score",
    title="ATS Score Comparison"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -----------------------------
# SEMANTIC VS SKILL
# -----------------------------

st.subheader(
    "🧠 Semantic vs Skill Match"
)

# Clean data BEFORE plotting

if df.empty:
    st.warning("No valid candidate scores found.")
    st.stop()

df = df[df["score"] > 0]

fig2 = px.scatter(
    df,
    x="semantic",
    y="skill",
    size="score",
    color="score",
    hover_name="filename",
    title="Candidate Distribution"
)



st.plotly_chart(
    fig2,
    use_container_width=True
)

# -----------------------------
# ATS DISTRIBUTION
# -----------------------------

st.subheader(
    "📊 ATS Score Distribution"
)

fig3 = px.histogram(
    df,
    x="score",
    nbins=10,
    title="ATS Score Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# -----------------------------
# TOP CANDIDATES
# -----------------------------

st.subheader(
    "🥇 Top Candidates"
)

top_df = df.sort_values(
    by="score",
    ascending=False
).head(5)

st.dataframe(
    top_df[
        [
            "filename",
            "score",
            "semantic",
            "skill",
            "matched",
        ]
    ],
    use_container_width=True
)

# -----------------------------
# SKILL ANALYSIS
# -----------------------------

st.subheader(
    "🛠 Most Common Matched Skills"
)

skills = []

for item in df.get("matched", []):

    if item:

        skills.extend(
            [
                s.strip()
                for s in item.split(",")
                if s.strip()
            ]
        )

if skills:

    skill_df = pd.DataFrame(
        pd.Series(skills)
        .value_counts()
    ).reset_index()

    skill_df.columns = [
        "skill",
        "Count"
    ]

    fig4 = px.bar(
        skill_df.head(10),
        x="skill",
        y="Count",
        title="Top Skills Found"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

else:

    st.info(
        "No skill data available."
    )

# -----------------------------
# RAW DATA
# -----------------------------

st.subheader(
    "📂 Complete Dataset"
)

st.dataframe(
    df,
    use_container_width=True
)

email = st.session_state.get(
    "user_email",
    "Unknown"
)

st.sidebar.markdown("---")

