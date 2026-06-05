from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_tfidf_similarity(
    resume_text,
    job_description
):

    documents = [
        resume_text,
        job_description
    ]

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(
        documents
    )

    score = cosine_similarity(
        matrix[0],
        matrix[1]
    )[0][0]

    return round(
        score * 100,
        2
    )