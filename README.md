# 🧠 Production-Grade RAG System (Ask My Docs)

A production-ready Retrieval-Augmented Generation (RAG) application that allows users to chat with documents using **hybrid retrieval (BM25 + vector search)**, **cross-encoder reranking**, and **citation-backed answers**.

Unlike basic RAG chatbots, this system follows patterns commonly used in enterprise AI applications to improve retrieval quality, reduce hallucinations, and increase answer reliability.

## 🚀 Live Demo

Streamlit App:

https://appuction-rag-ccejmm8xc3w4r4qsvwvmhw.streamlit.app/

# 📌 Features

### Hybrid Retrieval
Combines:

- **BM25 Search**
    - Keyword-based retrieval
    - Good for exact matches

- **Vector Search (FAISS)**
    - Semantic understanding
    - Finds contextually similar documents

Using both improves recall and answer quality.

---

### Cross Encoder Reranking

Retrieved documents are reranked using HuggingFace cross-encoder models to select the most relevant chunks before sending them to the LLM.

Improves:

✅ Relevance  
✅ Context accuracy  
✅ Final answer quality

---

### Citation Enforcement

Every generated response includes document references/citations to reduce hallucinations and increase trust.

Example:

Answer:
"Hybrid retrieval combines lexical and semantic search."

Sources:
- page_12.pdf
- docs_chunk_4

---

### Evaluation Pipeline

Automated evaluation checks:

- Retrieval quality
- Answer correctness
- Faithfulness
- Citation accuracy

Useful for CI/CD pipelines in production AI systems.

---

# 🏗 Architecture

User Query

↓

Hybrid Search

(BM25 + FAISS)

↓

Top-K Retrieval

↓

Cross Encoder Reranking

↓

Context Selection

↓

LLM Generation

↓

Citation-backed Response

---

# 🛠 Tech Stack

Frontend:

- Streamlit

Backend:

- Python
- LangChain

Retrieval:

- BM25
- FAISS

Embeddings:

- HuggingFace Embeddings

Reranking:

- HuggingFace Cross Encoder

LLM:

- Groq API (Free)

Evaluation:

- Custom Metrics / RAG Evaluation

Deployment:

- Streamlit Cloud / Render

---

# 💸 Fully Free Stack

This project was built using free/open-source tools:

| Component | Tool |
|----------|------|
| Vector DB | FAISS |
| Search | BM25 |
| Embeddings | HuggingFace |
| Reranker | HuggingFace |
| LLM | Groq |
| Deployment | Streamlit |
| Framework | LangChain |

Total Cost:

**₹0 / $0**

---

# 🌍 Real World Use Cases

This architecture can be used for:

- Company internal knowledge bases
- Legal document assistants
- Medical documentation systems
- Customer support chatbots
- Research assistants
- SOP search systems
- Enterprise AI copilots

---

# 📈 Future Improvements

Potential upgrades:

- Multi-agent workflows
- Query rewriting
- Memory support
- Multi-modal RAG
- SQL + document retrieval
- User authentication
- Feedback learning loop

---

# ⚙ Installation

Clone repository:

```bash
git clone YOUR_REPO_LINK
cd project-folder
