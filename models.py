from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

# 요청 모델 정의
class ChatRequest(BaseModel):
    query: str = Field(..., description="사용자 질문")
    beforeQuestionList: Optional[List[str]] = Field(
        default=None, description="이전 질문 목록"
    )
    beforeResponseList: Optional[List[str]] = Field(
        default=None, description="이전 대답 목록"
    )