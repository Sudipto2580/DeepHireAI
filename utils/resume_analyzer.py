from utils.skill_extractor import extract_skills

def analyze_resume_strength(resume_text):

    skills = extract_skills(resume_text)

    strengths = []
    weaknesses = []
    suggestions = []

    score = 50

    # Skills

    if len(skills) >= 5:

        strengths.append(
            "Strong technical skill coverage"
        )

        score += 15

    else:

        weaknesses.append(
            "Limited technical skills"
        )

        suggestions.append(
            "Add more job-relevant skills"
        )

    # Projects

    if "project" in resume_text.lower():

        strengths.append(
            "Projects section present"
        )

        score += 10

    else:

        weaknesses.append(
            "Projects section missing"
        )

        suggestions.append(
            "Add project descriptions"
        )

    # Experience

    if (
        "experience" in resume_text.lower()
        or
        "internship" in resume_text.lower()
    ):

        strengths.append(
            "Experience mentioned"
        )

        score += 10

    else:

        weaknesses.append(
            "No experience section"
        )

        suggestions.append(
            "Add internship or experience"
        )

    # Certifications

    if (
        "certification" in resume_text.lower()
        or
        "certificate" in resume_text.lower()
    ):

        strengths.append(
            "Certifications present"
        )

        score += 10

    else:

        weaknesses.append(
            "No certifications found"
        )

        suggestions.append(
            "Add Coursera, AWS, Google certifications"
        )

    # Contact

    if "@" in resume_text:

        strengths.append(
            "Email contact available"
        )

        score += 5

    else:

        weaknesses.append(
            "Email missing"
        )

    score = min(score,100)

    return {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }