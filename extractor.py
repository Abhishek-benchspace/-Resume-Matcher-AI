def extract_skills(text):
    known_skills = [
        "python", "java", "c++", "javascript", "r",
        "aws", "gcp", "azure", "docker", "kubernetes", "mlops",
        "pandas", "numpy", "matplotlib", "seaborn", "sklearn", "langchain",
        "mysql", "mongodb", "postgresql", "sqlite",
        "communication", "teamwork", "leadership", "design", "problem-solving"
    ]

    extracted = []
    text_lower = text.lower()
    for skill in known_skills:
        if skill in text_lower:
            extracted.append(skill)
    return extracted


def categorize_skills(skills):
    categories = {
        "Programming": ["python", "java", "c++", "javascript", "r"],
        "Cloud / DevOps": ["aws", "gcp", "azure", "docker", "kubernetes", "mlops"],
        "Tools / Libraries": ["pandas", "numpy", "matplotlib", "seaborn", "sklearn", "langchain"],
        "Databases": ["mysql", "mongodb", "postgresql", "sqlite"],
        "Soft Skills": ["communication", "teamwork", "leadership", "design", "problem-solving"]
    }

    categorized = {cat: [] for cat in categories}
    for skill in skills:
        for cat, keywords in categories.items():
            if skill.lower() in keywords:
                categorized[cat].append(skill)
                break
    return categorized
