from langchain_text_splitters import RecursiveCharacterTextSplitter

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def chunk_text(text):
    sentence_regex = r"(?<!\bMr)(?<!\bMrs)(?<!\bDr)(?<=[.!?])\s*"
    custom_rules = ["\n\n", "\n", sentence_regex, " ", ""]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators = custom_rules,
        keep_separator=True,
        is_separator_regex=True
    )
    chunks = text_splitter.split_text(text)
    return chunks