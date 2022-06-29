import uvicorn

if __name__ == "__main__":
    uvicorn.run("api_app:app", port=8081, host="0.0.0.0", reload=True)
