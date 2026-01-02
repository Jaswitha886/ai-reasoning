from langchain_community.vectorstores import Chroma
from core.embeddings.embedder import get_embedder

_vectorstore = None

def build_vectorstore(documents, persist_dir="./chroma_db"):
    global _vectorstore
    embeddings = get_embedder()
    _vectorstore = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    return _vectorstore

def get_vectorstore():
    if _vectorstore is None:
        raise RuntimeError("Vectorstore not initialized")
    return _vectorstore
