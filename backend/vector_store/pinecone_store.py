import uuid
from pinecone import Pinecone, ServerlessSpec
from backend.core.config import settings
from backend.embeddings.embedder import generate_embedding

pc = None
index = None

def init_pinecone():
    global pc, index

    if not settings.PINECONE_API_KEY:
        print("⚠️ Pinecone not configured. Running without vector DB.")
        return

    pc = Pinecone(api_key=settings.PINECONE_API_KEY)

    if settings.INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=settings.INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    index = pc.Index(settings.INDEX_NAME)

def store_text(text: str):
    if not index:
        return

    vector = generate_embedding(text)
    index.upsert([
        {
            "id": str(uuid.uuid4()),
            "values": vector,
            "metadata": {"text": text}
        }
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
