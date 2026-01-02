from tools.pdf_tool import load_pdf
from core.vectorstore.chroma_store import build_vectorstore
from config.settings import DATA_DIR

def ingest_documents():
    documents = []
    for pdf in DATA_DIR.glob("*.pdf"):
        documents.extend(load_pdf(str(pdf)))

    if not documents:
        raise RuntimeError("No documents found for ingestion")

    return build_vectorstore(documents)
