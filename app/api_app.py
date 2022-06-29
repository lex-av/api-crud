from fastapi import FastAPI
from src.db.base import database

app = FastAPI(
    title="EDU API",
    description="CRUD service",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
