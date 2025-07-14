# API 연동 테스트용 코드
from google import genai
from google.genai import types
from config import config  # 중앙화된 설정 사용

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="API 테스트야. 너는 정상적으로 API를 받고 있다면 너의 이름과 정보를 알려줘",
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # 생각중 없애기
    )
)
print(response.text)