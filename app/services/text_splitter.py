from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200):
    """
    Splits long transcript text into smaller chunks.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.create_documents([text])