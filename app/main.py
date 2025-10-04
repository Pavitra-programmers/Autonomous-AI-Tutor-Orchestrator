"""FastAPI app with endpoints."""

from fastapi import FastAPI
from app.orchestrator import orchestrate

app = FastAPI(title="AI Tutor Orchestrator", version="1.0.0")

@app.post("/orchestrate/message")
async def orchestrate_endpoint(payload: dict):
    """
    Main endpoint for processing student requests.
    Takes user_id and text, returns orchestrated response.
    """
    user_id = payload["user_id"]
    text = payload["text"]
    
    result = await orchestrate(user_id, text)
    return result

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}