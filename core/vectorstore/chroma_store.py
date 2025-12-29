import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(persist_directory="./chroma_db")
)

collection = client.get_or_create_collection("documents")

def add_document(doc_id: str, text: str, embedding: list):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[doc_id]
    )

def query_documents(query_embedding: list, top_k: int = 3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]
