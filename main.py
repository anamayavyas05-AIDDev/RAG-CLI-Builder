from document_loader import load_pdf
from chunker import chunk_text
from embeddings import generate_embeddings

if __name__ == "__main__":
    file_path = "data/book.pdf"
    text = load_pdf(file_path)
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)
    print(f"Number of chunks: {len(chunks)}")
    print(f"Shape of embeddings: {embeddings.shape}")
    print(f"First chunk: {chunks[0]}")
