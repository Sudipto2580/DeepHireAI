SKILLS = [

# Programming

"python",
"java",
"c++",
"c",
"javascript",
"typescript",
"go",
"rust",

# Database

"sql",
"mysql",
"postgresql",
"mongodb",
"oracle",

# Data Science

"numpy",
"pandas",
"matplotlib",
"seaborn",
"power bi",
"tableau",

# Machine Learning

"machine learning",
"deep learning",
"supervised learning",
"unsupervised learning",
"reinforcement learning",

# AI

"nlp",
"computer vision",
"transformers",
"bert",
"gpt",
"llm",
"generative ai",
"rag",
"langchain",

# Frameworks

"tensorflow",
"keras",
"pytorch",
"scikit-learn",

# Cloud

"aws",
"azure",
"gcp",

# DevOps

"docker",
"kubernetes",
"jenkins",
"github actions",

# Web

"html",
"css",
"react",
"angular",
"vue",
"node.js",
"express",

# Backend

"django",
"flask",
"fastapi",

# Mobile

"android",
"flutter",
"react native",

# Security

"cybersecurity",
"network security",
"penetration testing",

# Big Data

"hadoop",
"spark",

# MLOps

"mlops",
"airflow",
"kubeflow"

# AI

"nlp",
"computer vision",
"transformers",
"bert",
"gpt",
"llm",
"generative ai",
"rag",
"langchain",
"prompt engineering",
"agentic ai",
"crewai",
"autogen",
"gemini",
"openai",
"huggingface",
"faiss",
"chromadb",
"vector database",
"pinecone",
"embedding",
"fine tuning",
"lora",
"ai agent",
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return list(set(found))