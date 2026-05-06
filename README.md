# 🚀 Agentic RAG System (LLaMA 3 + LangGraph)

An **Agentic Retrieval-Augmented Generation (RAG)** system built using **LangChain + LangGraph**, supporting:

* 🔍 Intelligent document retrieval
* 🌐 Web search fallback (Tavily)
* 🧠 Self-correction (hallucination + answer grading)
* 🔀 Dynamic routing between vectorstore and web

---

# 📌 Features

* Adaptive RAG (routing queries)
* Corrective RAG (fallback to web search)
* Self-RAG (hallucination detection)
* Local LLM support (Ollama + LLaMA3)
* Vector database using ChromaDB
* Modular LangGraph workflow

---

# 🧰 Tech Stack

* Python 3.10+
* LangChain ecosystem
* LangGraph
* ChromaDB
* Tavily Search API
* Ollama (for local LLM)

---

# ⚠️ IMPORTANT (Before Running)

This project supports **TWO environments**:

## 🖥️ 1. LOCAL (Recommended for full features)

* Uses Ollama + LLaMA3
* Full agentic capabilities

## ☁️ 2. CLOUD (Streamlit / Render)

* ❌ Ollama NOT supported
* ✔ Use API-based LLM (Groq / OpenAI)

---

# 📦 Required Versions (VERY IMPORTANT)

Due to frequent updates in LangChain, use these versions:

```
python==3.10

langchain==0.1.20
langchain-community==0.0.38
langchain-core==0.1.52
langchain-text-splitters==0.0.1

chromadb==0.4.24
tiktoken==0.7.0
tavily-python==0.3.3

streamlit==1.35.0   # (only if using UI)
```

---

# 📥 Installation

## Step 1: Clone repo

```
git clone https://github.com/your-username/agentic-rag.git
cd agentic-rag
```

## Step 2: Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

## Step 3: Install dependencies

```
pip install -r requirements.txt
```

---

# 🤖 LOCAL SETUP (Ollama + LLaMA3)

## Install Ollama

👉 https://ollama.ai/

## Pull model:

```
ollama pull llama3
```

## Run:

```
python main.py
```

---

# ☁️ CLOUD DEPLOYMENT (Streamlit / Render)

## ⚠️ Important Limitation

* Ollama DOES NOT work in cloud
* Must replace with API model

---

## ✅ Use Groq (Recommended)

Install:

```
pip install langchain-groq
```

Replace LLM code:

```python
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key="YOUR_API_KEY"
)
```

---

## Run Streamlit App

```
streamlit run app.py
```

---

# 📂 Project Structure

```
agentic-rag/
│── main.py              # Core RAG agent
│── app.py               # Streamlit UI (optional)
│── requirements.txt
│── README.md
```

---

# 🔥 Common Errors & Fixes

## ❌ ModuleNotFoundError (LangChain)

Fix import:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

---

## ❌ "!pip install" SyntaxError

Remove from `.py` file
Run in terminal instead.

---

## ❌ Ollama not working in Streamlit

✔ Use Groq / OpenAI instead

---

# 🧠 Workflow

```
User Query
   ↓
Router (VectorDB or Web)
   ↓
Retriever
   ↓
LLM Generation
   ↓
Hallucination Check
   ↓
Final Answer
```

---

# 📊 Future Improvements

* Add memory (chat history)
* UI with chat interface
* Docker deployment
* Multi-document upload
* Urdu + English support (for Pakistan use case 🇵🇰)

---

# 👨‍💻 Author

**Zaheem Ahmed**
UI/UX Designer & MERN Stack Developer
📧 [zaheem808@gmail.com](mailto:zaheem808@gmail.com)

---

# ⭐ Support

If this project helps you:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---
