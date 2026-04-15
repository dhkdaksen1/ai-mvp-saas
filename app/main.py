from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    user_id: str
    text: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/ask")
def ask(req: Request):

    return {
        "user_id": req.user_id,
        "result": {
            "summary": f"요약: {req.text}",
            "insights": ["문제 분석", "기회 발견"],
            "action_plan": ["자동화 실행", "리포트 생성"]
        }
    }
