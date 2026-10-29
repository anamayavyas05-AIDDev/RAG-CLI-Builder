from pypdf import PdfReader
import re

def get_pdf_pages(file_path):
    reader = PdfReader(file_path)
    return len(reader.pages)

def parse_pdf(file_path, total_pages):
    reader = PdfReader(file_path)
    result = []
    for i in range(total_pages):
        if i==0:
            continue
        page = reader.pages[i]
        page_text = page.extract_text()
        result.append({"page_number": i, "text": page_text})
    return result

def load_pdf(file_path):
    if not file_path.endswith(".pdf"):
        raise ValueError("The provided file is not a PDF.") 
    total_pages = get_pdf_pages(file_path)
    result = parse_pdf(file_path, total_pages)
    return result