from typing import Literal

from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")
QUOTE_NOTIFICATION_EMAIL = os.getenv("QUOTE_NOTIFICATION_EMAIL")



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
    if not resend.api_key or not QUOTE_NOTIFICATION_EMAIL:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Email service is not configured.",
        )

    try:
        resend.Emails.send(
            {
                "from": "Clean Tangerine <onboarding@resend.dev>",
                "to": [QUOTE_NOTIFICATION_EMAIL],
                "subject": f"New quote request from {quote.name}",
                "html": f"""
                    <h2>New Clean Tangerine quote request</h2>
                    <p><strong>Name:</strong> {quote.name}</p>
                    <p><strong>Email:</strong> {quote.email}</p>
                    <p><strong>Phone:</strong> {quote.phone}</p>
                    <p><strong>Service:</strong> {quote.service}</p>
                    <p><strong>Details:</strong></p>
                    <p>{quote.message or "No additional details provided."}</p>
                """,
            }
        )
    except Exception as error:
        print("Email delivery failed:", error)

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The quote was valid, but the notification email could not be sent.",
        ) from error

    return {
        "message": "Quote request received successfully.",
        "customer_name": quote.name,
    }