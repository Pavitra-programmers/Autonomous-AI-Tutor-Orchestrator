"""FastAPI app with endpoints."""

from fastapi import FastAPI
from app.orchestrator import orchestrate

app = FastAPI()

@app.post("/orchestrate/message")
async def orchestrate_endpoint(payload: dict):
    user_id = payload["user_id"]
    text = payload["text"]
    
    result = await orchestrate(user_id, text)
    return result

@app.get("/health")
async def health():
    return {"status": "healthy"}