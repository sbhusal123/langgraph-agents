from langchain_community.vectorstores import Chroma

from langchain_ollama.embeddings import OllamaEmbeddings

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import VectorStoreRetriever

def load_text_file_to_chroma(
    file_path: str,
    collection_name: str,
    persist_directory: str='./chroma_store',
    embedding_model: str = 'nomic-embed-text:latest',
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> VectorStoreRetriever:
    # Load and split the PDF
    txt = TextLoader(file_path).load()

    embeding = OllamaEmbeddings(model=embedding_model)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    split_text = text_splitter.split_documents(documents=txt)

    # Save into Chroma
    vectordb = Chroma.from_documents(
        documents=split_text,
        embedding=embeding,
        persist_directory=persist_directory,
        collection_name=collection_name
    )
    
    # Return retriever
    return vectordb.as_retriever()


def get_retriever_for_collection(
    collection_name: str,
    persist_directory: str = './chroma_store',
    embedding_model: str = 'nomic-embed-text:latest',
) -> VectorStoreRetriever:
    embeding = OllamaEmbeddings(model=embedding_model)
    vectordb = Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=embeding
    )
    return vectordb.as_retriever()


if __name__ == "__main__":
    load_text_file_to_chroma(
        file_path='./documents/info.txt',
        collection_name='info'
    )
