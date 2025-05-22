import logging
from urllib.parse import urljoin
from fastapi import HTTPException
from app.core.config import settings
from app.schemas.paypal_schema import Product
from app.utils.decorators import handle_errors
from app.utils.http_utils import make_request

PAYPAL_BASE_URL = settings.PAYPAL_BASE_URL
PAYPAL_AUTH_ENDPOINT = settings.PAYPAL_AUTH_ENDPOINT
PAYPAL_PRODUCT_ENDPOINT = settings.PAYPAL_PRODUCT_ENDPOINT

logger = logging.getLogger(__name__)

class PaypalUrl:
    def __init__(self):
        self.base = PAYPAL_BASE_URL
        self.auth = urljoin(self.base, PAYPAL_AUTH_ENDPOINT)
        self.product = urljoin(self.base, PAYPAL_PRODUCT_ENDPOINT)

paypal_url = PaypalUrl()

@handle_errors
def get_access_token(
        client_id: str = settings.PAYPAL_CLIENT_ID,
        client_secret: str = settings.PAYPAL_CLIENT_SECRET
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