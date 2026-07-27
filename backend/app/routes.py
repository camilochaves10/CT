from fastapi import APIRouter, HTTPException, status

from app.email_service import send_quote_emails
from app.schemas import HealthResponse, QuoteRequest, QuoteResponse


router = APIRouter()


@router.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Clean Tangerine API",
    }


@router.get(
    "/health",
    response_model=HealthResponse,
)
def health_check() -> HealthResponse:
    return HealthResponse(status="healthy")


@router.post(
    "/quotes",
    response_model=QuoteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_quote(quote: QuoteRequest) -> QuoteResponse:
    try:
        send_quote_emails(quote)

    except Exception as error:
        print(f"Email delivery failed: {error}")

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The quote was valid, but the email notifications could not be sent.",
        ) from error

    return QuoteResponse(
        message="Quote request received successfully.",
        customer_name=quote.name,
    )