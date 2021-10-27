from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "version": "2.0.0"
    }