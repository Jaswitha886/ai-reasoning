from fastapi import APIRouter
from services.reasoning_service import verify_answer

router = APIRouter()

@router.post("/verify")
def verify(payload: dict):
    question = payload.get("question")
    if not question:
        return {"error": "question is required"}

    return verify_answer(question)
