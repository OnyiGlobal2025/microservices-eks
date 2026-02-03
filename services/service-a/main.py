from fastapi import FastAPI
import requests
import os

app = FastAPI()

SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service-b:8000")

@app.get("/")
def root():
    return {"service": "A", "message": "Hello from Service A"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/call-service-b")
def call_service_b():
    response = requests.get(f"{SERVICE_B_URL}/")
    return {
        "from": "service-a",
        "service-b-response": response.json()
    }
