import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from models.embedding_model import get_model

def create_vector_store(text):
    model = get_model()
    chunks = []

    chunk_size = 500

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    model = get_model()
    embeddings = model.encode(chunks)

    return embeddings, chunks


def retrieve_context(
    question,
    embeddings,
    chunks
):

    model = get_model()
    query_embedding = model.encode([question])

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = np.argsort(
        similarities
    )[-3:][::-1]

    context = ""

    for idx in top_indices:

        if idx < len(chunks):

            context += (
                chunks[idx]
                + "\n"
            )

    return context