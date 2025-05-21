from fastapi import FastAPI
from app.core.config import settings
from app.routers import paypal_api

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

app.include_router(paypal_api.auth_router, prefix=settings.API_V1_STR)