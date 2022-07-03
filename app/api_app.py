from fastapi import FastAPI
from src.db.base import database
from src.endpoints import endpoint_users

app = FastAPI(
    title="EDU API",
    description="CRUD service",
    version="1.0.0",
)
app.include_router(endpoint_users.router, prefix="/users", tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
