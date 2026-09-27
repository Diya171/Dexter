from fastapi import FastAPI
from app.core.llm import call_llm

app = FastAPI(title="Dexter — R&D Command Center")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-llm")
def test_llm():
    response = call_llm(
        system_prompt="You are a helpful assistant.",
        user_prompt="Say hello in exactly 5 words.",
    )
    return {"response": response}