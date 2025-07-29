import pdfplumber
from docx import Document

def extract_pdf_text(path):
    with pdfplumber.open(path) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def extract_docx_text(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_resume_text(path):
    ext = path.suffix.lower()
    if ext == ".pdf":
        return extract_pdf_text(path)
    elif ext == ".docx":
        return extract_docx_text(path)
    elif ext == ".txt":
        return open(path, 'r').read()
    else:
        raise ValueError("Unsupported file type")

def extract_jd_text(path):
    return extract_resume_text(path)
