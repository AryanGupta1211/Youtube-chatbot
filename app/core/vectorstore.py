from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def build_vector_store(documents):
    """
    Creates FAISS vector store from documents.
    """
    embeddings = OllamaEmbeddings(model="mistral")
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store