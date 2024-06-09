from langchain_community.embeddings.huggingface import (
    HuggingFaceInferenceAPIEmbeddings
)
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.document_loaders.base import Document
from langchain.chains.base import Chain
from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from typing import List
import os


def get_embeddings(model_name: str) -> GoogleGenerativeAIEmbeddings:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings


def similarity_search(query: str, faiss_index: FAISS, k: int = 5) -> List[Document]:
    docs = faiss_index.similarity_search(query, k=k)
    return docs