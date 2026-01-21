import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

def generate_response(user_query: str, context: str):
    prompt = f"""
You are Jarvis, a professional AI assistant.

Use the context only if it is helpful.

Context:
{context}

User Question:
{user_query}

Answer clearly and concisely:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    return response.json()["response"]
