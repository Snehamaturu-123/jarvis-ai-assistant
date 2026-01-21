from fastapi import FastAPI
from backend.api.chat_api import router
from backend.vector_store.pinecone_store import init_pinecone

app = FastAPI(title="Jarvis AI Assistant")

init_pinecone()
app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Jarvis is running"}
