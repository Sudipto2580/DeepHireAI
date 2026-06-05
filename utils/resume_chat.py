from utils.llm import ask_llm

from utils.rag import (
    create_vector_store,
    retrieve_context
)

def ask_resume_question(
    resume_text,
    question
):

    index, chunks = (
        create_vector_store(
            resume_text
        )
    )

    context = retrieve_context(
        question,
        index,
        chunks
    )

    prompt = f"""
You are an expert recruiter.

Resume Context:

{context}

Question:

{question}

Answer ONLY using the resume context.
"""

    return ask_llm(
        prompt
    )