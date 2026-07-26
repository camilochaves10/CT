from typing import Literal

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(title="Clean Tangerine API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuoteRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(min_length=7, max_length=30)
    service: Literal[
        "home-cleaning",
        "deep-cleaning",
        "office-cleaning",
    ]
    message: str = Field(default="", max_length=1000)


@app.get("/")
def root():
    return {"message": "Clean Tangerine API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/quotes", status_code=status.HTTP_201_CREATED)
def create_quote(quote: QuoteRequest):
    print("New quote request:", quote.model_dump())

    return {
        "message": "Quote request received successfully.",
        "customer_name": quote.name,
    }