from core.llm.ollama_client import call_llm
import json

def plan(query: str) -> dict:
    prompt = f"""
You are a planning agent in an AI reasoning system.

Classify the user query into ONE category:

- "concept" → definitions, explanations, theory
- "factual" → stored or document-based facts
- "external" → real-time or live information

Respond ONLY in valid JSON:
{{
  "query_type": "concept" | "factual" | "external"
}}

User query:
"{query}"
"""

    response = call_llm(prompt)

    try:
        result = json.loads(response)
    except Exception:
        result = {"query_type": "concept"}

    return {
        "query_type": result.get("query_type", "concept")
    }
