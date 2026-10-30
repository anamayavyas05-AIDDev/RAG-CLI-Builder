from pypdf import PdfReader
import re

def get_pdf_pages(file_path):
    reader = PdfReader(file_path)
    return len(reader.pages)

def clean_text(text):
    pattern1 = r"\nCHAPTER.*?\n.*?(?=\n)"
    pattern2 = r"^\d+\n"
    text = re.sub(pattern1, "", text, flags=re.DOTALL)
    text = re.sub(pattern2, "", text, flags=re.MULTILINE)
    text = re.sub(r'\n\s*\n', ' <PARAGRAPH> ', text)
    text = text.replace('\n', ' ')
    text = text.replace(' <PARAGRAPH> ', '\n\n')
    text = re.sub(r' +', ' ', text)
    return text.strip()

def parse_pdf(file_path, total_pages):
    reader = PdfReader(file_path)
    result =""
    for i in range(total_pages):
        if i==0:
            continue
        page = reader.pages[i]
        page_text = page.extract_text()
        result += " " + clean_text(page_text)
        # result.append({"page_number": i, "text": clean_text(page_text)})
    return result

def load_pdf(file_path):
    if not file_path.endswith(".pdf"):
        raise ValueError("The provided file is not a PDF.") 
    total_pages = get_pdf_pages(file_path)
    result = parse_pdf(file_path, total_pages)
    return result