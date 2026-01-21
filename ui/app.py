import streamlit as st
import requests

st.set_page_config(page_title="Jarvis AI")
st.title("🤖 Jarvis – AI Assistant")

query = st.text_input("Ask Jarvis:")

if st.button("Send"):
    if query.strip():
        res = requests.post(
            "http://localhost:8000/chat",
            params={"query": query}
        )
        st.success(res.json()["response"])
