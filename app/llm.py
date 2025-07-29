import os
import requests
from dotenv import load_dotenv
from app.model import MatchResult
import json
import re

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

def extract_json_from_string(s):
    # This regex finds the first {...} block in the string
    match = re.search(r'\{.*\}', s, re.DOTALL)
    if match:
        return match.group(0)
    raise ValueError("No JSON object found in string")

def get_match_analysis(resume, jd):
    prompt = f"""
You are a recruitment assistant. Match the resume with the job description.

Resume:
{resume}

Job Description:
{jd}

Return JSON in this format:
{{
  "match_score": 0-100,
  "top_skills_matched": ["..."],
  "red_flags": ["..."],
  "summary": "..."
}}
"""

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
        json={
            "model": GROQ_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
    )

    if res.status_code != 200:
        print("❌ API Error:", res.status_code)
        print(res.text)
        raise Exception("Groq API failed")

    try:
        response_json = res.json()
        content = response_json['choices'][0]['message']['content']
        json_str = extract_json_from_string(content)
        return MatchResult.model_validate_json(json_str).model_dump()

    except Exception as e:
        print("⚠️ Unexpected Response Format:")
        print(res.json())
        raise e
