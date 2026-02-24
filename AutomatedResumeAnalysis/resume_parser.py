import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
# import os

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text


def extract_keywords_from_job_description(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        jd_text = f.read()
        jd_text = jd_text.lower()
        jd_text = re.sub(r'[^a-z+\s]', '', jd_text)
        words = jd_text.split()
        words = [w for w in words if w not in stop_words]
        return set(words)

def clean_text(text):
    text = text.lower()
    # Keep letters, spaces, plus sign (for c++)
    text = re.sub(r'[^a-z+\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return words