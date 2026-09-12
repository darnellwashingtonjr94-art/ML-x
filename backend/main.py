from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router as ml_router

app = FastAPI(
    title="ML-x Inference API",
    description="Multi-framework ML backend",
    version="1.0.0"
)

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ml_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}
