import logging
from fastapi import HTTPException
from app.schemas.paypal_schema import Product, Plan, Subscription, PatchOperation, ListTransactionsQueryParams
from app.services.paypal.config import paypal_url
from app.utils.decorators import handle_errors
from app.utils.http_utils import make_request

logger = logging.getLogger(__name__)

# Auth
# ----------
@handle_errors
def get_access_token(
        client_id: str,
        client_secret: str
) -> str:
    access_token = make_request(
        method="POST",
        url=paypal_url.auth,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    ).get("access_token")
    if not access_token:
        raise HTTPException(status_code=500, detail="Failed to get access token")
    return access_token

# Product
# ----------
@handle_errors
def create_product(access_token: str, product: Product) -> dict:
    return make_request(
        method="POST",
        url=paypal_url.product,
        token=access_token,
        json=product.model_dump()
    )

@handle_errors
def list_products(access_token: str) -> dict:
    return make_request(
        method="GET",
        url=paypal_url.product,
        token=access_token
    )

@handle_errors
def show_product_details(access_token: str, product_id: str) -> dict:
    return make_request(
        method="GET",
        url=f"{paypal_url.product}/{product_id}",
        token=access_token
    )

# Plan
# ----------
@handle_errors
def create_plan(access_token: str, plan: Plan) -> dict:
    return make_request(
        method="POST",
        url=paypal_url.plan,
        token=access_token,
        json=plan.model_dump()
    )

@handle_errors
def list_plans(access_token: str) -> dict:
    return make_request(
        method="GET",
        url=paypal_url.plan,
        token=access_token
    )

@handle_errors
def show_plan_details(access_token: str, plan_id: str) -> dict:
    return make_request(
        method="GET",
        url=f"{paypal_url.plan}/{plan_id}",
        token=access_token
    )

# Subscription
# ----------
@handle_errors
def create_subscription(access_token: str, subscription: Subscription) -> dict:
    return make_request(
        method="POST",
        url=paypal_url.subscription,
        token=access_token,
        json=subscription.model_dump()
    )

@handle_errors
def show_subscription_details(access_token: str, subscription_id: str) -> dict:
    return make_request(
        method="GET",
        url=f"{paypal_url.subscription}/{subscription_id}",
        token=access_token
    )

@handle_errors
def update_subscription(access_token: str, subscription_id: str, update_request: list[PatchOperation]) -> dict:
    return make_request(
        method="PATCH",
        url=f"{paypal_url.subscription}/{subscription_id}",
        token=access_token,
        json=[operation.model_dump() for operation in update_request]
    )

@handle_errors
def list_transactions(access_token: str, subscription_id: str, query_params: ListTransactionsQueryParams) -> dict:
    return make_request(
        method="GET",
        url=f"{paypal_url.subscription}/{subscription_id}/transactions",
        token=access_token,
        params={"start_time": query_params.start_time, "end_time": query_params.end_time}
    )