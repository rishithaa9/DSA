Backend
    Python
    FastAPI
AI
    LangChain

OpenAI / Gemini API

Vector Database
    FAISS (local and free)

Frontend
    Streamlit (initially)
To create python virtual environment
 py -m venv venv
 python -m pip install --upgrade pip
 pip install langchain langchain-pdf langchain-community faiss-cpu pypdf sentence-transformers streamlit python-
pip install langchain-google-genai

PDF
↓
List[Document]
↓
Chunks
↓
Embeddings
↓
FAISS
↓
Question
↓
Question Embedding
↓
Similarity Search
↓
Top K Chunks
↓
LLM
↓
Answer

Notes:
FAISS = Facebook AI Similarity Search(Search engine for vectors)
Limitation of FAISS-it cannot understand text, it undetstands only numbers