from langchain_ollama import OllamaEmbeddings


def get_embeddings():

    embeddings = OllamaEmbeddings(model= "qwen3-embedding:4b ")

    return embeddings