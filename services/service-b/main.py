from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "B", "message": "Hello from Service B"}

@app.get("/health")
def health():
    return {"status": "ok"}
