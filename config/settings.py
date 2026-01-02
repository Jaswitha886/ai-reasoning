from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "documents"

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:latest"

TOP_K = 3
