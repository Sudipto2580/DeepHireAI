import streamlit as st
import pandas as pd

from utils.theme import load_theme
from utils.supabase_db import get_all_candidates

load_theme()

if not st.session_state.get("logged_in", False):
    st.switch_page("app.py")

st.title("🕒 Candidate History")

history = get_all_candidates()

if not history:
    st.warning("No records found.")
    st.stop()

df = pd.DataFrame(history)

df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
).fillna(0)

search = st.text_input(
    "Search Candidate"
)

if search:

    df = df[
        df["filename"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

min_score = st.slider(
    "Minimum ATS Score",
    0,
    100,
    0
)

df = df[
    df["score"] >= min_score
]

display_df = df[
    [
        "filename",
        "score",
        "semantic",
        "skill",
        "matched",
        "missing"
    ]
]

st.dataframe(
    display_df,
    use_container_width=True
)

st.download_button(
    "Download History CSV",
    data=display_df.to_csv(index=False),
    file_name="history.csv"
)