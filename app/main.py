from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "version": "1.0.0"
    }
