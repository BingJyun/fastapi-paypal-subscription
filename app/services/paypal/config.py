from urllib.parse import urljoin
from app.core.config import settings

PAYPAL_BASE_URL = settings.PAYPAL_BASE_URL
PAYPAL_AUTH_ENDPOINT = settings.PAYPAL_AUTH_ENDPOINT
PAYPAL_PRODUCT_ENDPOINT = settings.PAYPAL_PRODUCT_ENDPOINT
PAYPAL_PLAN_ENDPOINT = settings.PAYPAL_PLAN_ENDPOINT
PAYPAL_SUBSCRIPTION_ENDPOINT = settings.PAYPAL_SUBSCRIPTION_ENDPOINT

class PaypalUrl:
    def __init__(self):
        self.base = PAYPAL_BASE_URL
        self.auth = urljoin(self.base, PAYPAL_AUTH_ENDPOINT)
        self.product = urljoin(self.base, PAYPAL_PRODUCT_ENDPOINT)
        self.plan = urljoin(self.base, PAYPAL_PLAN_ENDPOINT)
        self.subscription = urljoin(self.base, PAYPAL_SUBSCRIPTION_ENDPOINT)

paypal_url = PaypalUrl()