import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import streamlit as st
from parsers import pdf_parser, docx_parser, txt_parser
from skills.job_roles_loader import load_job_roles
from skills import gap_analyzer
from skills.extractor import extract_skills, categorize_skills
from matchers import bert_matcher

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("📝 Resume Matcher with Skill Gap Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
job_role = st.selectbox("Select Job Role", ["Data Scientist", "AI Engineer", "Software Developer"])

if uploaded_file and job_role:
    file_type = uploaded_file.type

    # Extract text based on file type
    if file_type == "application/pdf":
        resume_text = pdf_parser.extract_pdf_text(uploaded_file)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = docx_parser.parse_docx(uploaded_file)
    elif file_type == "text/plain":
        resume_text = txt_parser.parse_txt(uploaded_file)
    else:
        st.error("Unsupported file format.")
        resume_text = ""

    if resume_text:
        # Extract and categorize skills
        extracted_skills = extract_skills(resume_text)
        categorized_skills = categorize_skills(extracted_skills)

        # Load job descriptions and extract job-specific skills
        job_roles = load_job_roles()
        job_description = job_roles.get(job_role, "")
        job_skills = extract_skills(job_description)

        # Skill gap analysis
        missing_skills = gap_analyzer.analyze_gaps(extracted_skills, job_skills)

        # Semantic match score
        match_score = bert_matcher.get_match_score(resume_text, [job_description])[0].item()

        # Display results
        st.subheader("✅ Match Score")
        st.success(f"Your resume matches {match_score * 100:.2f}% with the {job_role} role.")

        st.subheader("📌 Extracted Skills")
        st.write(extracted_skills)

        st.subheader("📂 Categorized Skills")
        st.json(categorized_skills)

        st.subheader("❗ Missing Skills for Selected Role")
        st.warning(missing_skills)
