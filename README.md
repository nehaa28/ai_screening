# 🧠 AI Resume Screening App (Groq + Python)

This is a lightweight, open-source resume screening assistant powered by **Groq** LLMs and free Python tools. It extracts resume text, compares it to a job description, and scores candidate fit using structured AI output.

## 🚀 Features

- ✅ Supports PDF, DOCX, TXT resumes
- ✅ Uses **Groq LLMs** (e.g., LLaMA 3 or Mixtral)
- ✅ Extracts structured results (match score, skills, red flags)
- ✅ Outputs to CSV or Google Sheets
- ✅ 100% open source

## 🛠️ Tech Stack

| Component         | Tool/Library              |
|------------------|---------------------------|
| LLM              | [Groq API](https://console.groq.com/) |
| File Parsing     | `pdfplumber`, `python-docx` |
| Prompt Parsing   | `pydantic` (v2)           |
| Output Storage   | `pandas` (CSV), `gspread` (optional) |
| Config Management| `dotenv`                  |

## 📁 Project Structure

```
resume-screening-ai/
├── app/
│   ├── main.py          # Main runner
│   ├── parser.py        # Resume + JD text extraction
│   ├── llm.py           # Groq API logic
│   ├── model.py         # Pydantic model for results
│   └── utils.py         # Save to CSV
├── data/
│   ├── resumes/         # Upload resume files here
│   ├── job\_descriptions/ # Upload JDs here
│   └── output.csv       # Output results
├── .env                 # API keys and configs
├── requirements.txt     # Python dependencies
└── README.md
````

## 🧪 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/resume-screening-ai.git
cd resume-screening-ai
````

### 2. Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama3-70b-8192
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 📄 Example Usage

Put a resume (e.g., `resume1.pdf`) in `data/resumes/`
Put a job description (e.g., `jd1.pdf`) in `data/job_descriptions/`

Then run:

```bash
python app/main.py
```

The app will:

* Extract text from both files
* Send it to Groq LLM
* Receive structured analysis
* Save results to `data/output.csv`

## 🧠 Sample Output

```json
{
  "match_score": 85,
  "top_skills_matched": ["Python", "FastAPI", "AWS"],
  "red_flags": ["No leadership experience"],
  "summary": "Candidate has 5+ years in backend development and strong cloud skills."
}
```

## 🧰 Optional Enhancements

* [ ] FastAPI Web UI for uploading resumes
* [ ] Google Sheets integration via `gspread`
* [ ] Support for bulk resume screening
* [ ] Stream responses from Groq

## 📜 License
MIT License

## 🙋 Support or Questions?

Open an issue or reach out at \[[nehaa.bansal94@gmail.com](mailto:nehaa.bansal94@gmail.com)].

**Built with ♥ using open source + Groq**

