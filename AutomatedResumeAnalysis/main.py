from resume_parser import extract_text_from_pdf,clean_text,extract_keywords_from_job_description
from score_calculator import calculate_score
from skill_matcher import load_skills, match_skills
import os


if __name__ == "__main__":
    if __name__ == "__main__":
        # resume_text = extract_text_from_pdf(r"C:\Users\ASUS\Downloads\your_resume.pdf")
        resume_text = extract_text_from_pdf(r"C:\Users\ASUS\Downloads\Shresth SDE  (1).pdf")

        skills = load_skills('skills.txt')
        jd_keywords = extract_keywords_from_job_description('job_description.txt')

        # Match with skills.txt (optional predefined skill set)
        found, missing = match_skills(resume_text, skills)
        score = calculate_score(found, skills)

        # Match with JD keywords
        resume_words = clean_text(resume_text)
        matched_jd = [word for word in resume_words if word in jd_keywords]
        jd_score = calculate_score(set(matched_jd), jd_keywords)

        print("📄 Matched Skills from skills.txt:", found)
        print("📉 Missing from skills.txt:", missing)
        print("✅ Skill Match Score:", score, "%")
        print("📌 Matched Keywords from JD:", matched_jd)
        print("📈 JD Match Score:", jd_score, "%")
