import os
from core.embeddings.embedder import embed_text
from core.vectorstore.chroma_store import add_document

DATA_DIR = "data/documents"

def ingest_documents():
    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            embedding = embed_text(text)
            add_document(file, text, embedding)
