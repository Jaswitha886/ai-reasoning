from agents.retriever_agent import retrieve

def get_context(query: str):
    return retrieve(query)
