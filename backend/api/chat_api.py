from fastapi import APIRouter
from backend.services.chat_service import handle_chat

router = APIRouter()

@router.post("/chat")
def chat_endpoint(query: str):
    response = handle_chat(query)
    return {"response": response}
