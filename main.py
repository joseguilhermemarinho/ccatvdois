# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRequest(BaseModel):
    user: str

@app.post("/auth/me")
def auth_me(user_request: UserRequest):
    return {"user": user_request.user, "ping": "pong"}