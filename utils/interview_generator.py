def generate_questions(skills):

    questions = []

    skill_questions = {

        "python": [
            "Explain Python decorators.",
            "What is the difference between List and Tuple?",
            "How does Python memory management work?"
        ],

        "sql": [
            "What is the difference between WHERE and HAVING?",
            "Explain SQL JOIN types.",
            "What are indexes in SQL?"
        ],

        "java": [
            "Explain OOP concepts in Java.",
            "What is JVM?",
            "Difference between Abstract Class and Interface?"
        ],

        "javascript": [
            "What is closure in JavaScript?",
            "Difference between var, let and const?",
            "Explain event bubbling."
        ],

        "machine learning": [
            "What is overfitting?",
            "Explain bias vs variance.",
            "What is cross validation?"
        ],

        "deep learning": [
            "Difference between CNN and RNN?",
            "What is backpropagation?",
            "Explain dropout."
        ],

        "tensorflow": [
            "What is TensorFlow?",
            "Explain TensorFlow graph execution.",
            "How do you save a model?"
        ],

        "aws": [
            "What AWS services have you used?",
            "Difference between EC2 and Lambda?",
            "What is S3?"
        ]
    }

    for skill in skills:

        skill = skill.lower()

        if skill in skill_questions:

            questions.extend(
                skill_questions[skill]
            )

    questions.extend([

        "Tell me about yourself.",

        "Describe a challenging project you completed.",

        "Why should we hire you?",

        "What are your career goals?",

        "Describe a situation where you solved a difficult problem."
    ])

    return questions[:15]