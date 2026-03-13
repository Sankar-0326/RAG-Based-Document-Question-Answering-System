from langchain_community.vectorstores import Chroma
import os

def create_vector_store(chunks, embeddings): 

    vectordb = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory= "vector_db"
    )

    return vectordb

def load_vector_store(embeddings):

    if not os.path.exists("vector_db"):
        raise FileNotFoundError("Vector DB directory does not exist")

    vectordb = Chroma(
        embedding_function=embeddings,
        persist_directory="vector_db"
    )

    if vectordb._collection.count() == 0:
        raise ValueError("Vector DB is empty")
    return vectordb