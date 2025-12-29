from agents.planner_agent import plan
from agents.verifier_agent import verify
from agents.synthesizer_agent import synthesize
from services.rag_service import get_context
import os

DOCS_PATH = "data/documents"

def documents_exist() -> bool:
    return os.path.exists(DOCS_PATH) and len(os.listdir(DOCS_PATH)) > 0

def run_reasoning_pipeline(query: str):
    plan_result = plan(query)
    query_type = plan_result["query_type"]

    use_rag = False
    use_tools = False

    # 🔒 SYSTEM POLICY (IMPORTANT)
    if query_type in ["concept", "factual"] and documents_exist():
        use_rag = True
    elif query_type == "external":
        use_tools = True

    context = None
    verification = None
    sources = []

    if use_rag:
        context = get_context(query)
        verification = verify(context)
        sources.append("local_documents")

        if verification and not verification["is_fresh"]:
            sources.append("possibly_outdated_data")

    answer = synthesize(query, context)

    return {
        "query": query,
        "decision": {
            "query_type": query_type,
            "use_rag": use_rag,
            "use_tools": use_tools
        },
        "sources": sources,
        "verification": verification,
        "answer": answer,
        "reasoning": (
            "Used retrieved documents to ground the answer."
            if use_rag
            else "Answered using internal model reasoning."
        )
    }
