# 🤖 Jarvis AI Assistant

Jarvis AI Assistant is a modular, self-hosted conversational AI application built using modern backend architecture.  
It integrates a FastAPI backend, a vector database for contextual memory, and a Streamlit-based user interface.  
The system is designed to be LLM-ready and can work with self-hosted models such as LLaMA via Ollama.



## 📌 Features

- Modular backend architecture (industry-style)
- Context-aware responses using vector memory
- Pinecone integration for semantic search (optional)
- Self-hosted AI model support (Ollama + LLaMA)
- Interactive chatbot UI using Streamlit
- Easy to extend and scale



## 🛠️ Tech Stack

- Backend: FastAPI
- Frontend: Streamlit
- AI / LLM: Local AI engine (LLM-ready, Ollama supported)
- Vector Database: Pinecone
- Embeddings: Sentence Transformers
- Language: Python
- Version Control: Git & GitHub



## 📂 Project Structure

```text
jarvis-ai-assistant/
│
├── backend/
│ ├── main.py
│ ├── api/
│ │ └── chat_api.py
│ ├── services/
│ │ └── chat_service.py
│ ├── ai/
│ │ ├── local_llm.py
│ │ └── ollama_llm.py
│ ├── embeddings/
│ │ └── embedder.py
│ ├── vector_store/
│ │ └── pinecone_store.py
│ ├── core/
│ │ └── config.py
│ └── requirements.txt
│
├── ui/
│ ├── app.py
│ └── requirements.txt
│
├── .env
├── README.md
└── run_project.md
```


OUTPUT:
<img width="1861" height="864" alt="image" src="https://github.com/user-attachments/assets/9ceb77c6-7ebf-4466-bac9-334ece9a9937" />





