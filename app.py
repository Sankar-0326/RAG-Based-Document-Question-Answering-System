from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from src.load_documents import load_documents
from src.split_documents import split_documents
from src.embeddings import get_embeddings
from src.vectordb import create_vector_store, load_vector_store
from src.rag_chain import create_rag_chain

load_dotenv()

rag_chain = None


class QuestionRequest(BaseModel):
    question: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    global rag_chain

    print("Initializing RAG system...")

    embeddings = get_embeddings()

    try:
        vectordb = load_vector_store(embeddings)
        print("Loaded existing vector database")

    except (FileNotFoundError, ValueError) as e:
        print(f"Could not load vector database ({e}), creating from scratch...")

        documents = load_documents("data/documents")

        if not documents:
            raise RuntimeError("No PDF documents found in data/documents/")

        chunks = split_documents(documents)
        vectordb = create_vector_store(chunks, embeddings)

    rag_chain = create_rag_chain(vectordb)

    print("RAG system ready")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/ask")
def ask_question(request: QuestionRequest):

    response = rag_chain.invoke(request.question)

    return {
        "question": request.question,
        "answer": response
    }
