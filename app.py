import streamlit as st
import pandas as pd
import pdfplumber
import docx
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load NLP model
# --- UTILITY FUNCTIONS ---

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_contact_info(text):
    email = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    phone = re.findall(r'[\+\d]?(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4})', text)
    return (email[0] if email else "Not Found"), (phone[0] if phone else "Not Found")

def extract_skills(text):
    # Predefined common skills list (Expandable)
    skill_db = [
        "Python", "Java", "C++", "JavaScript", "SQL", "Tableau", "Power BI", "Excel",
        "Machine Learning", "Data Analysis", "React", "Node.js", "Docker", "AWS",
        "Project Management", "Leadership", "Communication", "Agile", "Scrum",
        "Git", "TensorFlow", "PyTorch", "NLP", "Pandas", "NumPy", "Scikit-Learn"
    ]
    extracted = [skill for skill in skill_db if skill.lower() in text.lower()]
    return list(set(extracted))

def extract_education(text):
    edu_keywords = ["Bachelor", "Master", "B.Tech", "M.Tech", "B.E", "B.Sc", "MBA", "PhD", "University", "College"]
    lines = text.split('\n')
    education = [line.strip() for line in lines if any(kw.lower() in line.lower() for kw in edu_keywords)]
    return list(set(education))[:3] # Return top 3 matches

def get_ats_score(resume_text, jd_text):
    documents = [resume_text, jd_text]
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    return round(cosine_similarity(vectors)[0][1] * 100, 2)

# --- UI COMPONENTS ---

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer & ATS Scorer")
st.markdown("Optimize your resume or rank multiple candidates with ease.")

tab1, tab2 = st.tabs(["Analyze Resume", "Resume Ranking (Batch)"])

with tab1:
    st.header("Single Resume Analysis")
    jd_input = st.text_area("Paste Job Description (JD) here:", height=200)
    uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

    if st.button("Analyze") and uploaded_file and jd_input:
        # Extract Text
        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)
        
        # Extraction Logic
        email, phone = extract_contact_info(resume_text)
        skills = extract_skills(resume_text)
        education = extract_education(resume_text)
        ats_score = get_ats_score(resume_text, jd_input)
        
        # JD Skills (for missing skills check)
        jd_skills = extract_skills(jd_input)
        missing_skills = [s for s in jd_skills if s not in skills]

        # Display Results
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Candidate Info")
            st.write(f"**Email:** {email}")
            st.write(f"**Phone:** {phone}")
            st.write(f"**Education:** {', '.join(education) if education else 'Not detected'}")
            
        with col2:
            st.subheader("ATS Match Score")
            st.metric(label="Match Percentage", value=f"{ats_score}%")
            if ats_score > 70:
                st.success("High match! Your resume aligns well.")
            else:
                st.warning("Low match. Consider tailoring your resume.")

        st.subheader("Skills Analysis")
        st.write(f"**Detected Skills:** {', '.join(skills)}")
        if missing_skills:
            st.error(f"**Missing Skills:** {', '.join(missing_skills)}")
        else:
            st.success("All JD-related skills found!")

        st.subheader("Improvement Suggestions")
        suggestions = []
        if len(resume_text.split()) < 300: suggestions.append("Consider adding more detail; your resume is quite short.")
        if not education: suggestions.append("Clearly state your educational background.")
        if missing_skills: suggestions.append(f"Incorporate missing keywords: {', '.join(missing_skills[:3])}...")
        
        for s in suggestions:
            st.info(f"💡 {s}")

with tab2:
    st.header("Candidate Ranking System")
    jd_batch = st.text_area("Job Description for Ranking:", height=150, key="batch_jd")
    batch_files = st.file_uploader("Upload Multiple Resumes", type=["pdf", "docx"], accept_multiple_files=True)

    if st.button("Rank Resumes") and batch_files and jd_batch:
        results = []
        for file in batch_files:
            text = extract_text_from_pdf(file) if file.name.endswith(".pdf") else extract_text_from_docx(file)
            score = get_ats_score(text, jd_batch)
            email, _ = extract_contact_info(text)
            results.append({"Candidate Name": file.name, "Email": email, "Match Score (%)": score})
        
        df = pd.DataFrame(results).sort_values(by="Match Score (%)", ascending=False)
        st.table(df)
        st.balloons()