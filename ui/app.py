import streamlit as st
import requests

st.set_page_config(page_title="Jarvis – AI Assistant", layout="centered")
st.title("🤖 Jarvis – AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input (THIS FIXES THE DUPLICATION ISSUE)
user_input = st.chat_input("Ask Jarvis...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    response = requests.post(
        "http://localhost:8000/chat",
        params={"query": user_input}
    )

    jarvis_reply = response.json()["response"]

    # Add assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": jarvis_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(jarvis_reply)
