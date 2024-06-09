from langchain_community.document_loaders.dataframe import DataFrameLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.document_loaders.base import Document
from typing import List
import pandas as pd


def create_faiss_index(index_path: str, embeddings) -> None:
    df = pd.read_csv("./data/spotify_millsongdata.csv")
    loader = DataFrameLoader(df.sample(4000), page_content_column="text")
    docs = loader.load()
    faiss_index = FAISS.from_documents(docs, embeddings)
    faiss_index.save_local(index_path)
    return faiss_index


def load_faiss_index(index_path: str, embeddings) -> FAISS:
    return FAISS.load_local(index_path, embeddings=embeddings,
                            allow_dangerous_deserialization=True)
