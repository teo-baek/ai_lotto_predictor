from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.lotto_router import router as lotto_router

app = FastAPI(title="AI Lotto Predictor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lotto_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "AI Lotto Predictor Backend is running 🚀"}
