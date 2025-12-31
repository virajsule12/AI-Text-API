from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.openai_client import classify_text

router = APIRouter()

class ClassifyRequest(BaseModel):
    text: str
    labels: list[str]

@router.post("/")
def classify(req: ClassifyRequest):
    try:
        result = classify_text(req.text, req.labels)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
