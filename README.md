# TaleCraft-AI
TaleCraft의 AI서버입니다.
## 배포방법
서버 실행 후 python과 git 및 라이브러리 설치
```
# python 설치
pip install python3

# git 설치
pip install git

# git으로 프로젝트 복사
git clone https://github.com/MTVS-TaleCraft/TaleCraft-AI.git

# 가상환경 생성 (권장)
python -m venv venv  # Windows : py -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# .env.example 복사
cp .env.example .env

# .env 내부의 환경변수 설정
# GEMINI_API_KEY: Google AI Studio 발급
GEMINI_API_KEY=your_gemini_api_key_here

# 필수 의존성 라이브러리 설치
pip install -r requirements.txt

# 실행 테스트
uvicorn chatbot:app --reload --host 0.0.0.0 --port 8000

# 백그라운드 실행
nohup uvicorn chatbot:app --host 0.0.0.0 --port 8000 > output.log 2>&1 &
```
