from fastapi import APIRouter
from services.reasoning_service import run_reasoning_pipeline

router = APIRouter()

@router.post("/query")
def query_ai(payload: dict):
    question = payload.get("query")
    result = run_reasoning_pipeline(question)
    return result
