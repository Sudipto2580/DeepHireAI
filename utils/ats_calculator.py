from sklearn.metrics.pairwise import cosine_similarity

from models.embedding_model import get_embedding

def calculate_ats_score(
        resume_text,
        job_description
):

    resume_embedding = get_embedding(
        resume_text
    )

    jd_embedding = get_embedding(
        job_description
    )

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(score * 100,2)