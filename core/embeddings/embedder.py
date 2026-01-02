from langchain_community.embeddings import OllamaEmbeddings
from config.settings import EMBEDDING_MODEL

def get_embedder():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)
