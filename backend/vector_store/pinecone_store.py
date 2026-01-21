import pinecone
import uuid
from backend.core.config import settings
from backend.embeddings.embedder import generate_embedding

index = None

def init_pinecone():
    global index

    if not settings.PINECONE_API_KEY:
        print("⚠️ Pinecone not configured. Running without vector DB.")
        return

    pinecone.init(
        api_key=settings.PINECONE_API_KEY,
        environment=settings.PINECONE_ENV
    )

    if settings.INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(
            name=settings.INDEX_NAME,
            dimension=384,
            metric="cosine"
        )

    index = pinecone.Index(settings.INDEX_NAME)

def store_text(text: str):
    if not index:
        return

    vector = generate_embedding(text)
    index.upsert([
        (str(uuid.uuid4()), vector, {"text": text})
    ])

def search_text(query: str, top_k=3):
    if not index:
        return ""

    query_vector = generate_embedding(query)
    result = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    return " ".join(
        match["metadata"]["text"]
        for match in result["matches"]
    )
