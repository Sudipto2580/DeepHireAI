# 🚀 DeepHire AI
## AI-Powered Recruitment Intelligence Platform

DeepHire AI is an intelligent recruitment platform designed to automate and enhance the hiring process using Artificial Intelligence, Machine Learning, Natural Language Processing (NLP), and Large Language Models (LLMs).

The platform helps recruiters and HR professionals analyze resumes, rank candidates, generate interview questions, evaluate ATS compatibility, and gain recruitment insights through interactive analytics dashboards.

---
## 🌟 Key Features

### 📄 ATS Resume Screening

* Resume parsing and text extraction
* ATS score calculation
* Semantic similarity analysis
* TF-IDF similarity scoring
* Skill gap identification
* Candidate recommendations

### 🤖 AI Recruitment Assistant

* AI-powered recruitment support
* Candidate evaluation assistance
* Job description understanding
* Recruitment guidance

### 🎤 AI Interviewer

* Automatic interview question generation
* Technical interview preparation
* HR interview assistance
* Candidate assessment support

### 📊 Recruitment Analytics Dashboard

* Candidate ranking visualization
* ATS score comparison charts
* Skill analysis dashboard
* Recruitment performance metrics
* Hiring insights

### 📂 Candidate History Management

* Candidate database storage
* Search and filtering
* Historical analysis
* CSV export functionality

### 👤 User Management

* Secure authentication
* User profiles
* Personalized settings
* Theme customization

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ├── ATS Analysis Engine
 ├── Analytics Dashboard
 ├── AI Recruiter
 ├── AI Interviewer
 └── Resume Assistant
 │
 ▼
Business Logic Layer
 │
 ├── Resume Parser
 ├── Skill Extractor
 ├── ATS Calculator
 ├── TF-IDF Similarity
 ├── Candidate Ranking
 └── Recommendation Engine
 │
 ▼
Supabase Cloud Database
 │
 ▼
Google Gemini AI
```

---

## 🛠 Technology Stack

### Frontend

* Streamlit
* Plotly

### Backend

* Python

### Artificial Intelligence

* Google Gemini 2.5 Flash
* Sentence Transformers
* Natural Language Processing (NLP)

### Machine Learning

* TF-IDF Vectorization
* Cosine Similarity
* Semantic Matching

### Database

* Supabase

### Data Processing

* Pandas
* NumPy

### PDF Processing

* PyMuPDF
* PyPDF

---

## 📁 Project Structure

```text
DeepHireAI/
│
├── app.py
├── assets/
├── models/
├── pages/
├── reports/
├── utils/
├── requirements.txt
└── README.md
```

---

## 📊 ATS Scoring Methodology

The final ATS score is calculated using a weighted combination of:

### Semantic Similarity

Measures contextual similarity between resume and job description.

**Weight:** 50%

### Skill Matching

Measures overlap between required skills and candidate skills.

**Weight:** 30%

### TF-IDF Similarity

Measures keyword relevance and matching.

**Weight:** 20%

### Final Formula

Final ATS Score =

(0.5 × Semantic Score)

* (0.3 × Skill Match Score)

* (0.2 × TF-IDF Score)

---

## 🔒 Security

* Password hashing using SHA-256
* Secure cloud database storage
* Environment variable protection
* Authentication-based access control

---

## 🎯 Objectives

* Automate resume screening
* Reduce manual hiring effort
* Improve recruitment efficiency
* Enhance candidate evaluation
* Provide explainable hiring decisions
* Enable AI-assisted recruitment

---

## 🚀 Future Enhancements

* LinkedIn Integration
* Resume OCR Support
* Video Interview Analysis
* Candidate Personality Assessment
* AI Recruitment Forecasting
* Multi-Organization Support
* Real-Time Collaboration

---

## 👨‍💻 Developer

**Sudipto Bairagi**

B.Tech – Computer Science and Engineering

Dr. B. R. Ambedkar National Institute of Technology, Jalandhar

Aspiring AI & Machine Learning Engineer

---

## 📜 License

This project is developed for educational, research, internship, and portfolio purposes.

---

## ⭐ Acknowledgements

* Google Gemini AI
* Supabase
* Streamlit
* Plotly
* Hugging Face
* Open Source Community
