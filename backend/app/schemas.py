from typing import Literal

from pydantic import BaseModel, EmailStr, Field


ServiceType = Literal[
    "home-cleaning",
    "deep-cleaning",
    "office-cleaning",
]


class QuoteRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        examples=["Camilo Chaves"],
    )

    email: EmailStr = Field(
        examples=["customer@example.com"],
    )

    phone: str = Field(
        min_length=7,
        max_length=30,
        examples=["(415) 555-1234"],
    )

    service: ServiceType

    message: str = Field(
        default="",
        max_length=2000,
        examples=["I would like a quote for a two-bedroom apartment."],
    )


class QuoteResponse(BaseModel):
    message: str
    customer_name: str


class HealthResponse(BaseModel):
    status: str