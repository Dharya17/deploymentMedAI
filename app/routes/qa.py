from fastapi import APIRouter
from pydantic import BaseModel
from app.services.qa_chain import get_response

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def ask_question(request: QueryRequest):
    result, sources = get_response(request.question)
    return {"answer": result, "sources": [doc.metadata.get('source', '') for doc in sources]}
