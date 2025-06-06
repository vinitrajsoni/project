import pdfplumber
import re
from io import BytesIO

def extract_resume_data(file: BytesIO):
    with pdfplumber.open(file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text)
    }

def extract_name(text):
    return text.split('\n')[0]

def extract_email(text):
    match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
    return match.group(0) if match else ""


def extract_phone(text):
    pattern = r'(\+91[\-\s]?|0)?[6789]\d{9}'
    match = re.search(pattern, text)
    return match.group(0) if match else ""


def extract_skills(text):
    skills = [
    'Python', 'Java', 'C++', 'Machine Learning', 'Data Analysis', 'SQL',
    'JavaScript', 'TypeScript', 'React', 'Angular', 'Vue.js', 'Node.js', 'Express',
    'Django', 'Flask', 'Ruby on Rails', 'PHP', 'Laravel', 'Swift', 'Kotlin',
    'AWS', 'Azure', 'Google Cloud', 'Docker', 'Kubernetes', 'Terraform',
    'Linux', 'Git', 'HTML', 'CSS', 'Sass', 'Bootstrap', 'TensorFlow', 'PyTorch',
    'Pandas', 'NumPy', 'Matplotlib', 'Seaborn', 'Tableau', 'Power BI', 'Hadoop',
    'Spark', 'Kafka', 'REST API', 'GraphQL', 'NoSQL', 'MongoDB', 'Redis', 'Elasticsearch',
    'Jenkins', 'CI/CD', 'Agile', 'Scrum','Communication', 'Teamwork', 'Problem Solving', 'Leadership',
    'Time Management', 'Adaptability', 'Creativity', 'Critical Thinking',
    'Work Ethic', 'Interpersonal Skills', 'Conflict Resolution',
    'Emotional Intelligence', 'Negotiation', 'Decision Making',
    'Attention to Detail', 'Collaboration', 'Flexibility', 'Self Motivation']

    found = [skill for skill in skills if skill.lower() in text.lower()]
    return found

def extract_experience(text):
    exp_start = text.lower().find("experience")
    if exp_start == -1:
        return ""
    return text[exp_start:exp_start+1000]
