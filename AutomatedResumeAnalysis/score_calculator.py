def calculate_score(found_skills, total_skills):
    if not total_skills:
        return 0
    return int((len(found_skills) / len(total_skills))*100)