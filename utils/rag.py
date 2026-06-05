from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(text):

    chunks = []

    chunk_size = 500

    for i in range(
        0,
        len(text),
        chunk_size
    ):
        chunks.append(
            text[i:i+chunk_size]
        )

    embeddings = model.encode(
        chunks
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(
            embeddings
        ).astype("float32")
    )

    return index, chunks


def retrieve_context(
    question,
    index,
    chunks
):

    query_embedding = model.encode(
        [question]
    )

    distances, indices = index.search(
        np.array(
            query_embedding
        ).astype("float32"),
        3
    )

    context = ""

    for idx in indices[0]:

        if idx < len(chunks):

            context += (
                chunks[idx]
                + "\n"
            )

    return context