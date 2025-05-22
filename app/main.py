import logging
from fastapi import FastAPI
from app.core.config import settings
from app.routers import paypal_api

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

app.include_router(paypal_api.auth_router, prefix=settings.API_V1_STR)
app.include_router(paypal_api.product_router, prefix=settings.API_V1_STR)