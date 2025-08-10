from rag import ask
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_endpoint(query: Query):
    print("User: " + query.question + "\n")
    answer = ask(query.question)
    print("5Array: " + answer + '\n')
    return {"answer":answer}