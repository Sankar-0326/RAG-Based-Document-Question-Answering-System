from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

def format_docs(docs):
    """
    Convert retrieved Document objects into a single text string
    """
    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain(vectordb):
    """
    Create the RAG pipeline
    """

    
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOllama(model= "wizardlm2:7b ")

    prompt = ChatPromptTemplate.from_template(
        """
        You are an assistant answering questions using the provided context.

        Context:
        {context}

        Question:
        {question}

        Answer the question based only on the context.
        """
    )

    # Build RAG chain using LCEL
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
