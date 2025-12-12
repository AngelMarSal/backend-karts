from fastapi import FastAPI
from app.database import engine

app = FastAPI(title="Karts API")

@app.get("/")
async def root():
    return {"message": "Hello World"}