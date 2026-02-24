def load_skills(file_path='skills.txt'):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(skill.strip().lower() for skill in f if skill.strip())

def match_skills(resume_text, skill_set):
    resume_text = resume_text.lower()
    found = []
    missing = []
    for skill in skill_set:
        if skill in resume_text:
            found.append(skill)
        else:
            missing.append(skill)
    return found, missing
