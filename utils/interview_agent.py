from utils.llm import ask_llm


def generate_interview_questions(
    job_role,
    skills
):

    prompt = f"""
You are a senior technical recruiter.

Job Role:
{job_role}

Candidate Skills:
{skills}

Generate:

1. Three technical questions
2. Two project questions
3. Two HR questions

Format clearly.
"""

    return ask_llm(prompt)


def evaluate_candidate(
    questions,
    answers
):

    prompt = f"""
You are a senior interviewer.

Questions:

{questions}

Candidate Answers:

{answers}

Evaluate:

1. Technical Knowledge (/10)
2. Communication Skills (/10)
3. Problem Solving Ability (/10)
4. Overall Score (/10)

Also provide:

Strengths
Weaknesses
Hiring Recommendation
"""

    return ask_llm(prompt)