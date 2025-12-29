from core.embeddings.embedder import embed_text
from core.vectorstore.chroma_store import query_documents

def retrieve(query: str):
    embedding = embed_text(query)
    return query_documents(embedding)
