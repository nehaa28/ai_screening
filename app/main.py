from app.parser import extract_resume_text, extract_jd_text
from app.llm import get_match_analysis
import os
import pandas as pd
from pathlib import Path
import json
import re

def save_to_csv(result, file='results.csv'):
    # Convert result to DataFrame
    df_new = pd.DataFrame([result])
    # Check if file exists and is not empty
    if not os.path.isfile(file) or os.stat(file).st_size == 0:
        # Write with header if file doesn't exist or is empty
        df_new.to_csv(file, index=False)
    else:
        # Append without writing the header
        df_new.to_csv(file, mode='a', header=False, index=False)

def extract_json_from_string(s):
    # This regex finds the first {...} block in the string
    match = re.search(r'\{.*\}', s, re.DOTALL)
    if match:
        return match.group(0)
    raise ValueError("No JSON object found in string")

def main():
    resume_path = Path("data/resumes/1.pdf")
    jd_path = Path("data/jd/jd_sales.pdf")

    resume_text = extract_resume_text(resume_path)
    jd_text = extract_jd_text(jd_path)

    print("🧠 Sending to Groq...")
    result = get_match_analysis(resume_text, jd_text)

    print("✅ Result:", result)
    save_to_csv(result)

if __name__ == "__main__":
    main()
