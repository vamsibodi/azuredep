from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to FastAPI RAG Project Backend",
        "status": "Application Running Successfully",
        "framework": "FastAPI",
        "deployment": "Azure Ready",
        "author": "Vamsi Achiever"
    }