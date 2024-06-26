from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.document_loaders.base import Document
from typing import List
import streamlit as st

def get_embeddings(model_name: str) -> GoogleGenerativeAIEmbeddings:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=st.secrets["GOOGLE_API_KEY"])
    return embeddings


def similarity_search(query: str, faiss_index: FAISS, k: int = 5) -> List[Document]:
    docs = faiss_index.similarity_search(query, k=k)
    return docs