from pathlib import Path
from dotenv import load_dotenv
import os
import resend
from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BACKEND_DIR / ".env"

load_dotenv(ENV_FILE)


class Settings(BaseSettings):
    resend_api_key: str
    quote_notification_email: EmailStr

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()

settings.resend_api_key
settings.quote_notification_email