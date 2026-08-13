# AI-RESUME-SCREENER
Domain Based AI Resume Screener

An automated tool built with Python to screen candidate resumes against domain-specific job descriptions using local Large Language Model (LLM) inference.


## 📌 What This Project Does
Screening dozens of resumes manually takes a lot of time. This project automates the first round of resume parsing and evaluation—specifically designed around specialized domain roles like Healthcare and Clinical Pharmacy.

Instead of relying on cloud APIs or basic keyword matching, this script runs a local LLM to read the resume, compare it to a detailed job description, and output a structured candidate analysis with scores and key recommendations.


## 🛠️ Tech Stack & Tools
* **Python**
* **Ollama** (Running `qwen2.5:1.5b` locally)
* **PyMuPDF (`fitz`)** (For extracting text from PDF resumes)
* **JSON Parsing & Regex** (For cleaning raw model outputs)


## 💡 How It Works
1. **PDF Text Extraction:** Uses PyMuPDF to extract raw text from candidate PDF resumes.
2. **Contextual Evaluation:** Sends the extracted text along with the target job description to a local Ollama model (`qwen2.5:1.5b`).
3. **Structured Analysis:** Prompt engineering forces the model to strictly evaluate key areas like education, clinical experience, research, and technical skills.
4. **Clean JSON Output:** Sanitizes the raw model response into a structured JSON summary containing match scores, missing critical skills, and an overall hiring recommendation.


## 🔒 Privacy & Local Processing
Because this tool uses **Ollama** locally on device, candidate data and resumes never leave your computer or get sent to third-party cloud services.


## 🚀 How to Run Locally

1. **Install Ollama** and pull the Qwen model:
   ```bash
   ollama run qwen2.5:1.5b
