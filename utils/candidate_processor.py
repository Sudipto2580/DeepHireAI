from utils.skill_extractor import extract_skills
from utils.ats_calculator import calculate_ats_score
from utils.tfidf_similarity import (
    calculate_tfidf_similarity
)

def process_candidate(
    resume_text,
    job_description
):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    matched_skills = list(
        set(resume_skills) &
        set(job_skills)
    )

    missing_skills = list(
        set(job_skills) -
        set(resume_skills)
    )

    semantic_score = calculate_ats_score(
        resume_text,
        job_description
    )

    tfidf_score = calculate_tfidf_similarity(
    resume_text,
    job_description
)

    if len(job_skills) == 0:
        skill_score = 0
    else:
        skill_score = (
            len(matched_skills)
            /
            len(job_skills)
        ) * 100

    final_score = (
        semantic_score * 0.5
        + skill_score * 0.3
        + tfidf_score * 0.2
    )

    print("Resume Skills:", resume_skills)
    print("Job Skills:", job_skills)
    print("Matched:", matched_skills)
    print("Missing:", missing_skills)

    return {
        "final_score": float(round(final_score, 2)),
        "semantic_score": float(round(semantic_score, 2)),
        "skill_score": float(round(skill_score, 2)),
        "tfidf_score": float(round(tfidf_score, 2)),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }