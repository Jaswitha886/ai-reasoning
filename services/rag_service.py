from langchain_community.llms import Ollama
from core.vectorstore.chroma_store import get_vectorstore
from config.settings import LLM_MODEL, TOP_K

llm = Ollama(model=LLM_MODEL)

def rag_answer(question: str) -> str:
    store = get_vectorstore()
    docs = store.similarity_search(question, k=TOP_K)

    context = "\n".join(d.page_content for d in docs)

    prompt = f"""
    Answer the question ONLY using the context.

    Context:
    {context}

    Question:
    {question}
    """

    return llm.invoke(prompt)
