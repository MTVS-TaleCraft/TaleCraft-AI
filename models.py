from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

# 요청 모델 정의
class ChatRequest(BaseModel):
    question: str = Field(..., description="사용자 질문")
    image: Optional[str] = Field(default=None, description="이미지 정보")
    beforeQuestionList: Optional[List[str]] = Field(
        default=None, description="이전 질문 목록"
    )
    beforeResponseList: Optional[List[str]] = Field(
        default=None, description="이전 대답 목록"
    )
    extensionLength: Optional[int] = Field(default=None, description="늘려야 될 길이")

class ChatResponse(BaseModel):
    status: bool = Field(..., description= "성공 여부")
    response: str = Field(..., description= "답변 내용")