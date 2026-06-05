import streamlit as st
from sentence_transformers import SentenceTransformer

@st.cache_resource
def get_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

def get_embedding(text):
    model = get_model()
    return model.encode(text)