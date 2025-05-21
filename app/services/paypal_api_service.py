import requests
from app.core.config import settings
from urllib.parse import urljoin


PAYPAL_BASE_URL = settings.PAYPAL_BASE_URL
PAYPAL_AUTH_ENDPOINT = settings.PAYPAL_AUTH_ENDPOINT
PAYPAL_PRODUCT_ENDPOINT = settings.PAYPAL_PRODUCT_ENDPOINT

def make_request(
        method: str,
        url: str,
        headers: dict,
        data: dict | None = None,
        auth: tuple | None = None
) -> dict:
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            auth=auth
        )
        response.raise_for_status()
        response_json = response.json()
    except requests.exceptions.HTTPError as e:
        raise Exception(f"Request failed: {e}")
    
    return response_json

def generate_access_token(
        client_id: str = settings.PAYPAL_CLIENT_ID,
        client_secret: str = settings.PAYPAL_CLIENT_SECRET
) -> str:
    response_json = make_request(
        method="POST",
        url=urljoin(PAYPAL_BASE_URL, PAYPAL_AUTH_ENDPOINT),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    )
    access_token = response_json.get("access_token")

    return access_token