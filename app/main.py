from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="YouTube Transcript Q&A API",
    description="Extracts transcript from YouTube and answers questions using Ollama + LangChain",
    version="1.0.0"
)

app.include_router(router)