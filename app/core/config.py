from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )

    API_V1_STR: str

    PAYPAL_BASE_URL: str
    PAYPAL_AUTH_ENDPOINT: str
    PAYPAL_PRODUCT_ENDPOINT: str

    PAYPAL_CLIENT_ID: str
    PAYPAL_CLIENT_SECRET: str

settings = Settings()