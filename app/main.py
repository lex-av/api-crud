import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", port=8081, host="0.0.0.0", reload=True)
