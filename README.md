# AI Reasoning System (Local, Agent-Based)

## Overview

**AI Reasoning** is a local, agent-based AI backend system that demonstrates how modern AI applications **decide how to answer a query**, not just generate text.

Instead of relying on a single LLM prompt, this system integrates:
- Query intent classification
- Retrieval-Augmented Generation (RAG)
- Agent-based reasoning
- Policy enforcement
- Data freshness verification

The system is designed to showcase **engineering thinking, modular design, and explainable AI workflows**, making it suitable for internship-level evaluation.

---

## Key Idea

> The LLM does not answer immediately.  
> The system first decides *how* the answer should be produced.

---

## System Architecture

The system is composed of clearly separated layers:

### 1. Planner Agent
- Classifies the user query into one of three types:
  - **Concept** (definitions, explanations)
  - **Factual** (document-based information)
  - **External** (real-time or live data)
- Does not generate answers.

### 2. Policy Layer
- Enforces system rules:
  - Concept and factual queries use **RAG** if local documents exist.
  - External queries use **tools**.
- Prevents uncontrolled LLM behavior.

### 3. RAG Layer
- Retrieves relevant information from local `.txt` documents.
- Uses embeddings and vector similarity search.
- Provides grounding context to the LLM.

### 4. Verifier Agent
- Validates retrieved context.
- Detects potentially outdated information by analyzing year references.
- Flags freshness issues explicitly.

### 5. Synthesizer Agent
- Generates the final response.
- Grounds answers in retrieved context when available.
- Produces clear, user-facing output.

---

## Reasoning Flow (Step-by-Step)

1. User sends a query to the API.
2. Planner agent classifies the query type.
3. System policy decides whether to use RAG or tools.
4. If RAG is enabled:
   - Relevant documents are retrieved.
   - Freshness is verified.
5. Synthesizer agent generates the final answer.
6. System returns:
   - Decision details
   - Sources used
   - Verification status
   - Final answer
   - Reasoning explanation

---

## Technologies Used

- **FastAPI** – API framework
- **Ollama** (Llama 3.2) – Local LLM runtime
- **ChromaDB** – Vector database
- **Sentence Transformers** – Embedding generation
- **Python** – Core implementation

---

## How to Run

```bash
pip install -r requirements.txt
python -m services.ingestion_service
uvicorn api.main:app --reload
```