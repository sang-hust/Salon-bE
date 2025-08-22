from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field("Salon Booking API", alias="APP_NAME")
    env: str = Field("dev", alias="ENV")
    secret_key: str = Field(..., alias="SECRET_KEY")
    access_token_expire_minutes: int = Field(120, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    database_url: str = Field("sqlite:///./app.db", alias="DATABASE_URL")

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
