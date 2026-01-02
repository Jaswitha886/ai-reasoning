import sys
from pathlib import Path

# ✅ Add project root to PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from fastapi import FastAPI
from api.routes import router
from services.ingestion_service import ingest_documents

app = FastAPI(title="AI Answer Verification System")

@app.on_event("startup")
def startup():
    ingest_documents()

app.include_router(router)
