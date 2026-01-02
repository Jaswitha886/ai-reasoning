from services.rag_service import rag_answer
from tools.web_tool import web_search

def verify_answer(question: str):
    rag = rag_answer(question)
    web = web_search(question)

    verdict, confidence, explanation = compare(rag, web)

    return {
        "question": question,
        "rag_answer": rag,
        "web_answer": web,
        "verdict": verdict,
        "confidence": confidence,
        "explanation": explanation
    }

def compare(rag: str, web: str):
    if rag.strip().lower() == web.strip().lower():
        return "VERIFIED", 0.9, "Both sources agree."

    return "CONFLICT", 0.4, "RAG and Web answers differ."
