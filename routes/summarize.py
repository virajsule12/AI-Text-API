from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.openai_client import summarize_text

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/")
def summarize(req: TextRequest):
    try:
        summary = summarize_text(req.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
