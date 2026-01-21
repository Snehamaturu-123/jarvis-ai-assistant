from backend.vector_store.pinecone_store import (
    store_text,
    search_text
)
from backend.ai.local_llm import generate_response

def handle_chat(query: str):
    context = search_text(query)
    response = generate_response(query, context)
    store_text(query + " " + response)
    return response
