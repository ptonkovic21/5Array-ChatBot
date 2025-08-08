from rag import ask
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_endpoint(query: Query):
    print("User: " + query.question + "\n")
    answer = ask(query.question)
    print("5Array: " + answer + '\n')
    return {"answer":answer}