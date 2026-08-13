import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
import ollama

def screen_resume(resume_text, job_description):
    prompt = f"""
You are a Senior Healthcare Recruiter with 20 years of experience hiring Clinical Pharmacists, PharmD Graduates, Pharmacovigilance Associates, Clinical Research Coordinators, Medical Writers, Regulatory Affairs Associates, and Hospital Pharmacists.

Your goal is to objectively evaluate a candidate's resume against the given healthcare job description.

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume_text}

TASK:

Analyze the candidate's resume carefully.

Evaluate:
- Educational qualification
- Clinical knowledge
- Pharmacology knowledge
- Hospital internship experience
- Clinical rotations
- Pharmacovigilance knowledge
- Medical writing skills
- Research experience
- Communication skills
- Technical skills
- Certifications
- Soft skills

Identify:
- Candidate's strengths
- Missing critical skills
- Whether the candidate is suitable for the role
- Any recommendations for improvement

Be strict but fair.

Return ONLY valid JSON.

JSON Format:

{{
    "candidate_name": "Candidate Name",
    "match_score": 0,
    "education": "Education summary",
    "experience": "Experience summary",
    "key_strengths": [
        "Strength 1",
        "Strength 2",
        "Strength 3"
    ],
    "missing_critical_skills": [
        "Skill 1",
        "Skill 2"
    ],
    "recommendation": "Interview" or "Reject",
    "reasoning": "Explain why the candidate received this score in 2-3 sentences."
}}

Do not return markdown.
Do not return explanation.
Return JSON only.
"""
    
    response = ollama.chat(model='qwen2.5:1.5b', messages=[
        {'role': 'user', 'content': prompt},
    ])
    
    return response['message']['content']
import json

# 1. Define the Job Description (The Standard)
job_description = """
Job Title: Clinical Pharmacist (PharmD)

Requirements:

- Doctor of Pharmacy (PharmD)
- Strong knowledge of Pharmacology
- Medication Therapy Management (MTM)
- Patient Counseling
- Clinical Rotations
- Hospital Internship
- Drug Interaction Analysis
- Adverse Drug Reaction (ADR) Reporting
- Clinical Documentation
- Good Communication Skills

Preferred:

- Pharmacovigilance
- Clinical Research
- Medical Writing
- Regulatory Affairs
- Electronic Health Records (EHR)
- Knowledge of NABH/JCI Standards

Responsibilities:

- Review prescriptions
- Monitor patient medications
- Detect drug interactions
- Counsel patients
- Collaborate with physicians
- Prepare clinical reports
- Ensure safe and effective medication use
"""

# 2. Load the Resume (The Input)
try:
    resume_text = extract_text_from_pdf(r"sample_resume.pdf")
    print(f"Resume loaded. Length: {len(resume_text)} characters.")
except Exception as e:
    print(f"Error loading resume: {e}")
    exit()

# 3. The Screening (The Processing)
print("AI is analyzing the candidate... (this may take a few seconds on local hardware)")
result_json_string = screen_resume(resume_text, job_description)

# 4. Parse and Display Results
try:
    # Sometimes LLMs wrap JSON in ```json blocks. We clean that up.
    clean_json = result_json_string.replace("```json", "").replace("```", "").strip()
    result_data = json.loads(clean_json)
    
    print("\n--- SCREENING REPORT ---")
    print(f"Candidate: {result_data.get('candidate_name', 'Unknown')}")
    print(f"Score: {result_data.get('match_score')}/100")
    print(f"Decision: {result_data.get('recommendation').upper()}")
    print(f"Reasoning: {result_data.get('reasoning')}")
    print(f"Missing Skills: {', '.join(result_data.get('missing_critical_skills', []))}")
    
except json.JSONDecodeError:
    print("Failed to parse JSON. Raw output:")
    print(result_json_string)        