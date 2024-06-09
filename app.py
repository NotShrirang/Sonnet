import streamlit as st
from dotenv import load_dotenv

from core.inference import get_embeddings, similarity_search
from core.db import load_faiss_index
from core.song import show_songs
import time


load_dotenv()

st.set_page_config(page_title='Sonnet', page_icon='🎵', layout="wide")

@st.cache_resource
def load_vectorstore():
    embeddings = get_embeddings("models/embedding-001")
    faiss_index = load_faiss_index('vectorstores/sonnetdb', embeddings)
    return faiss_index

faiss_index = load_vectorstore()

def inference(text: str):
    results = similarity_search(text, faiss_index, k=4)
    with st.chat_message("user"):
        st.write(text)
    with st.chat_message("assistant"):
        st.write_stream(stream_text("Here are some songs you might like:"))
        show_songs(results)

def stream_text(text: str):
    for char in text:
        time.sleep(0.01)
        yield char

st.title('Sonnet')
st.subheader("Hello! I'm Sonnet, your music assistant. How can I help you today?")
c1, c2, c3  = st.columns(3)

with st.spinner("waiting"):
    btn1 = c1.button("Give me a song about a dog.")
    if btn1:
        inference("Give me a song about a dog.")

    btn2 = c2.button("Song suggestions for a rainy day.")
    if btn2:
        inference("Song suggestions for a rainy day.")

    btn3 = c3.button("Suggest songs for a party.")
    if btn3:
        inference("Suggest songs for a party.")

text = st.chat_input("Write something...")

if text:
    with st.spinner("waiting"):
        inference(text)
