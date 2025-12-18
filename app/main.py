from fastapi import FastAPI
from app.database import engine

app = FastAPI(title="Karts API")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login", response_model=Token)
async def login():
    return ' d'