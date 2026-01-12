from fastapi import FastAPI
from routes import summarize, classify

app = FastAPI(
    title="AI Text Analysis API",
    root_path="/ai-text-analyzer" 
    )

# Include route modules
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])
app.include_router(classify.router, prefix="/classify", tags=["Classify"])


@app.get("/health")
def health():
    return {"status": "ok"}

