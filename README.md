# 📄 AI Resume Analyzer & ATS Scorer

An AI-powered Resume Analyzer built using Python, Streamlit, NLP, and Machine Learning. The application extracts key information from resumes, compares resumes against job descriptions, calculates ATS match scores, identifies missing skills, ranks candidates, and provides resume improvement suggestions.

---

## 🚀 Features

✅ Upload Resume (PDF/DOCX)

✅ Extract Candidate Information
- Email
- Phone Number
- Education
- Skills

✅ Resume vs Job Description Matching

✅ ATS Match Score Calculation

✅ Missing Skills Detection

✅ Resume Improvement Suggestions

✅ Multiple Resume Ranking System

✅ Interactive Streamlit Dashboard

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-Learn
- SpaCy
- PDFPlumber
- Python-Docx
- NLP
- TF-IDF Vectorization
- Cosine Similarity

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Download SpaCy Model

```bash
python -m spacy download en_core_web_sm
```

### Run Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

### Resume Parsing
Extracts text from PDF and DOCX resumes using PDFPlumber and Python-Docx.

### Information Extraction
Automatically extracts:
- Email Address
- Phone Number
- Education Details
- Technical Skills

### ATS Score Calculation
Uses:
- TF-IDF Vectorization
- Cosine Similarity

to compare the resume with the Job Description and generate a match score.

### Skill Gap Analysis
Identifies skills present in the Job Description but missing from the resume.

### Resume Ranking
Ranks multiple resumes based on ATS Match Score.

---

## 📊 Sample Output

### Candidate Information

```text
Email: candidate@gmail.com
Phone: 9876543210
Education: B.Tech Computer Science
```

### ATS Score

```text
Match Score: 82%
```

### Detected Skills

```text
Python
SQL
Machine Learning
NLP
Git
```

### Missing Skills

```text
Docker
AWS
TensorFlow
```

### Suggestions

```text
Add missing technical skills.
Include more project details.
Improve keyword alignment with the job description.
```

---

## 🔮 Future Enhancements

- AI-based Resume Feedback using LLMs
- Resume PDF Report Generation
- Advanced Skill Extraction
- Candidate Recommendation System
- Resume Keyword Optimization

---

## 👩‍💻 Author

**Anjali Upadhyay**  
B.Tech Computer Science & Engineering  
Galgotias University

---

## 📜 License

This project is developed for educational and recruitment assessment purposes.
