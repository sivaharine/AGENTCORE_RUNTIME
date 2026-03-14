from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .agent_core import agent_execute

app = FastAPI()
#instance for application

app.add_middleware(
    CORSMiddleware, #CORS middleware allows browser-based requests.
    allow_origins=["*"],#Allow requests from any frontend domain.
    allow_methods=["*"],#Allow all HTTP methods:GET,POST,PUT,DEL
    allow_headers=["*"],#Allow all request headers.
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    return agent_execute(request.message)
