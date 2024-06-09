from langchain_community.vectorstores.faiss import FAISS
from langchain_core.document_loaders.base import Document
from typing import List


def create_faiss_index(docs: List[Document], index_path: str, embeddings) -> None:
    faiss_index = FAISS.from_documents(docs, embeddings)
    faiss_index.save_local(index_path)


def load_faiss_index(index_path: str, embeddings) -> FAISS:
    return FAISS.load_local(index_path, embeddings=embeddings,
                            allow_dangerous_deserialization=True)