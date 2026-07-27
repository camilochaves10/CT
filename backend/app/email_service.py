from html import escape

import resend

from app.config import settings
from app.schemas import QuoteRequest


resend.api_key = settings.resend_api_key

SENDER_EMAIL = "Clean Tangerine <onboarding@resend.dev>"


def format_service_name(service: str) -> str:
    """Convert 'deep-cleaning' into 'Deep Cleaning'."""
    return service.replace("-", " ").title()


def send_business_notification(quote: QuoteRequest) -> None:
    service_name = format_service_name(quote.service)

    resend.Emails.send(
        {
            "from": SENDER_EMAIL,
            "to": [str(settings.quote_notification_email)],
            "reply_to": quote.email,
            "subject": f"New quote request from {quote.name}",
            "html": f"""
                <h2>New Clean Tangerine quote request</h2>

                <p><strong>Name:</strong> {escape(quote.name)}</p>
                <p><strong>Email:</strong> {escape(str(quote.email))}</p>
                <p><strong>Phone:</strong> {escape(quote.phone)}</p>
                <p><strong>Service:</strong> {escape(service_name)}</p>

                <p><strong>Customer message:</strong></p>
                <p>{escape(quote.message) if quote.message else "No additional details provided."}</p>
            """,
        }
    )


def send_customer_confirmation(quote: QuoteRequest) -> None:
    service_name = format_service_name(quote.service)

    resend.Emails.send(
        {
            "from": SENDER_EMAIL,
            "to": [str(quote.email)],
            "subject": "We received your Clean Tangerine quote request",
            "html": f"""
                <h2>Thanks for contacting Clean Tangerine, {escape(quote.name)}.</h2>

                <p>
                    We received your request for
                    <strong>{escape(service_name)}</strong>.
                </p>

                <p>
                    We'll review your information and follow up as soon as possible.
                </p>

                <p><strong>Your message:</strong></p>
                <p>{escape(quote.message) if quote.message else "No additional details provided."}</p>

                <p>
                    Thank you,<br>
                    <strong>Clean Tangerine</strong>
                </p>
            """,
        }
    )


def send_quote_emails(quote: QuoteRequest) -> None:
    """Send both emails associated with a quote request."""
    send_business_notification(quote)
    send_customer_confirmation(quote)