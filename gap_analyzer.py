def analyze_gaps(candidate_skills, required_skills):
    """
    Compares extracted skills with job role skills and returns missing ones.
    """
    candidate_skills_set = set([skill.lower() for skill in candidate_skills])
    required_skills_set = set([skill.lower() for skill in required_skills])
    return list(required_skills_set - candidate_skills_set)
