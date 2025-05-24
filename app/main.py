import logging
from fastapi import FastAPI
from app.core.config import settings
from app.routers import paypal_api

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    root_path=settings.API_V1_STR
)

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

app.include_router(paypal_api.auth_router)
app.include_router(paypal_api.product_router)
app.include_router(paypal_api.plan_router)
app.include_router(paypal_api.subscription_router)