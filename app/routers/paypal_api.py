import logging
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from app.schemas.paypal_schema import Product, Plan, Subscription
from app.schemas.api_response import LoginResponse
from app.services.paypal.api_service import (
    get_access_token,
    create_product, list_products, show_product_details,
    create_plan, list_plans, show_plan_details,
    create_subscription, show_subscription_details, update_subscription
)

logger = logging.getLogger(__name__)

security = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Auth
# ----------
auth_router = APIRouter(tags=["auth"], prefix="/auth")

@auth_router.post("", response_model=LoginResponse)
def get_access_token_route(credentials: HTTPBasicCredentials = Depends(security)):
    client_id = credentials.username
    client_secret = credentials.password
    access_token = get_access_token(client_id, client_secret)
    return {
        "message": "Access token generated successfully",
        "access_token": access_token
    }

# Product
# ----------
product_router = APIRouter(tags=["product"], prefix="/product")

@product_router.post("", response_model=dict)
def create_product_route(product: Product, access_token: str = Depends(oauth2_scheme)):
    return create_product(access_token, product)

@product_router.get("", response_model=dict)
def list_products_route(access_token: str = Depends(oauth2_scheme)):
    return list_products(access_token)

@product_router.get("/{product_id}", response_model=dict)
def show_product_details_route(product_id: str, access_token: str = Depends(oauth2_scheme)):
    return show_product_details(access_token, product_id)

# Plan
# ----------
plan_router = APIRouter(tags=["plan"], prefix="/plan")

@plan_router.post("", response_model=dict)
def create_plan_route(plan: Plan, access_token: str = Depends(oauth2_scheme)):
    return create_plan(access_token, plan)

@plan_router.get("", response_model=dict)
def list_plans_route(access_token: str = Depends(oauth2_scheme)):
    return list_plans(access_token)

@plan_router.get("/{plan_id}", response_model=dict)
def show_plan_details_route(plan_id: str, access_token: str = Depends(oauth2_scheme)):
    return show_plan_details(access_token, plan_id)

# Subscription
# ----------
subscription_router = APIRouter(tags=["subscription"], prefix="/subscription")

@subscription_router.post("", response_model=dict)
def create_subscription_route(subscription: Subscription, access_token: str = Depends(oauth2_scheme)):
    return create_subscription(access_token, subscription)

@subscription_router.get("/{subscription_id}", response_model=dict)
def show_subscription_details_route(subscription_id: str, access_token: str = Depends(oauth2_scheme)):
    return show_subscription_details(access_token, subscription_id)

@subscription_router.patch("/{subscription_id}", response_model=dict)
def update_subscription_route(subscription_id: str, update_request: list[dict], access_token: str = Depends(oauth2_scheme)):
    return update_subscription(access_token, subscription_id, update_request)