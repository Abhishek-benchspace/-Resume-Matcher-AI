from docx import Document

def extract_docx_text(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])
