# 📄 RAG-based Document Question Answering System

A **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions over a collection of PDF documents.
The system retrieves relevant document chunks using semantic search and generates answers using an LLM.

---

## 🚀 Features

* 📂 Load PDF documents from local directory
* ✂️ Intelligent text chunking using Recursive Character Splitter
* 🧠 Semantic embeddings using Ollama
* 🗄️ Persistent vector storage with ChromaDB
* 🔍 Top-k (k=3) semantic retrieval
* 🤖 LLM-powered question answering (RAG pipeline)
* ⚡ FastAPI-based API for interaction

---

## 🏗️ Project Structure

```
.
├── app.py
├── data/
│   └── documents/        # Input PDFs
├── vector_db/            # Persistent vector database
├── src/
│   ├── load_documents.py
│   ├── split_documents.py
│   ├── embeddings.py
│   ├── vectordb.py
│   └── rag_chain.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. **Load Documents**

   * PDFs are loaded using `PyPDFLoader`

2. **Split Documents**

   * Chunk size: `1000`
   * Overlap: `200`
   * Uses `RecursiveCharacterTextSplitter`

3. **Generate Embeddings**

   * Model: `qwen3-embedding:4b` (via Ollama)

4. **Store in Vector DB**

   * ChromaDB is used to persist embeddings

5. **Retriever**

   * Fetches **top 3 most relevant chunks**

6. **RAG Chain**

   * Combines retrieved context + user query
   * Generates answer using LLM (`wizardlm2:7b`)

---

## 🧰 Prerequisites

### 1. Install Ollama

Download and install Ollama:

👉 https://ollama.com/download

---

### 2. Pull Required Models

Run the following commands:

```bash
ollama pull qwen3-embedding:4b
ollama pull wizardlm2:7b
```

---

## 🐍 Setup Instructions

### 1. Clone Repository

```bash
git clone git@github.com:Sankar-0326/RAG-Based-Document-Question-Answering-System.git
cd RAG-Based-Document-Question-Answering-System
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

---

### 3. Activate Virtual Environment

#### Mac/Linux:

```bash
source venv/bin/activate
```

#### Windows:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Upload docs in data/documents

 ```bash
  data/documents/
 ```

---
## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

---

## 📡 API Usage

### Endpoint

```
POST /ask
```

### Request Body

```json
{
  "question": "Your question here"
}
```

### Example using cURL

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d '{"question": "What is this document about?"}'
```

---

## 🔁 Workflow Summary

```
PDFs → Load → Split → Embed → Store (Chroma)
                              ↓
                        Retrieve Top-3
                              ↓
                    Context + Question
                              ↓
                          LLM Answer
```

---

## ⚠️ Notes

* Ensure PDFs are placed inside:

  ```
  data/documents/
  ```
* Vector DB is persisted in:

  ```
  vector_db/
  ```
* If vector DB does not exist, it will be created automatically
* If empty, system rebuilds embeddings

---

## 🧠 Models Used

| Purpose    | Model              |
| ---------- | ------------------ |
| Embeddings | qwen3-embedding:4b |
| LLM (Chat) | wizardlm2:7b       |

---

## 🛠️ Tech Stack

* FastAPI
* LangChain
* ChromaDB
* Ollama
* Python

---

## 📌 Future Improvements

* Add support for multiple file types (TXT, DOCX)
* UI interface (Streamlit / React)
* Hybrid search (keyword + semantic)
* Metadata filtering

---

## 🙌 Acknowledgements

Built using LangChain and Ollama ecosystem for local LLM-powered applications.
