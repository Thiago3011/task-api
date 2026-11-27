from fastapi import FastAPI

app = FastAPI(title="Task API")


@app.get("/")
def home():
    return {"message": "Task API is running!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
