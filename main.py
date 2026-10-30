from document_loader import load_pdf
from chunker import chunk_text

if __name__ == "__main__":
    file_path = "data/book.pdf"
    text = load_pdf(file_path)
    chunks = chunk_text(text)
    for i, chunk in enumerate(chunks[:3]):
        print(f"=== CHUNK {i+1} ({len(chunk)} chars) ===")
        print(chunk)
        print("=" * 30 + "\n")
    # print(chunks[0])
    # print(f"Total Chunks Created: {len(chunks)}\n")clear

