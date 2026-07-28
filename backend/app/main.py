from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router


app = FastAPI(
    title="Clean Tangerine API",
    description="Backend API for Clean Tangerine quote requests.",
    version="1.0.0",
)

allowed_origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "https://ct-eight-ashy.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)