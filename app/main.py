from fastapi import FastAPI

app = FastAPI(
    title="Advanced Log Monitoring Platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Advanced Log Monitoring Platform Running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }