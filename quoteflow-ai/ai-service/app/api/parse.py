from fastapi import APIRouter

from app.schemas.quotation import AiRequest, AiResponse
from app.services.deepseek_service import chat

router = APIRouter()


@router.post("/api/callAi", response_model=AiResponse)
async def send_ai(request: AiRequest):

    result = await chat(request.message)

    return AiResponse.model_validate_json(result)