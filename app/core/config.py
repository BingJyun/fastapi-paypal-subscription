from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )

    PROJECT_NAME: str
    API_V1_STR: str

    PAYPAL_BASE_URL: str
    PAYPAL_AUTH_ENDPOINT: str
    PAYPAL_PRODUCT_ENDPOINT: str
    PAYPAL_PLAN_ENDPOINT: str
    PAYPAL_SUBSCRIPTION_ENDPOINT: str

    PAYPAL_CLIENT_ID: str
    PAYPAL_CLIENT_SECRET: str

    DB: str = "postgresql"
    DB_NAME: str = "my_db"
    DB_USER: str = "myuser"
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"

    @property
    def DB_URL(self) -> str:
        return f"{self.DB}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()