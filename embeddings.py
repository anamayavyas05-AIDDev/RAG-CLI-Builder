from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

def generate_embeddings(chunks):
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return embeddings