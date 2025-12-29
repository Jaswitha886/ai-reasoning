from core.llm.ollama_client import call_llm

def synthesize(query: str, context: list | None):
    prompt = f"""
Question:
{query}

Context:
{context if context else "No external context"}

Answer clearly and concisely.
"""
    return call_llm(prompt)
