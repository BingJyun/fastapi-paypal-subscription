from pydantic import BaseModel

class Product(BaseModel):
    name: str
    type: str
    id: str | None = None
    description: str | None = None
    category: str | None = None
    image_url: str | None = None
    home_url: str | None = None

class Plan(BaseModel):
    product_id: str
    name: str
    billing_cycles: list
    payment_preferences: dict
    status: str | None = "ACTIVE"
    description: str | None = None
    quantity_supported: bool | None = False
    taxes: dict | None = None

class Subscription(BaseModel):
    plan_id: str
    quantity: str | None = None
    auto_renewal: bool | None = False
    custom_id: str | None = None
    start_time: str | None = None
    shipping_amount: dict | None = None
    subscriber: dict | None = None
    application_context: dict | None = None
    plan: dict | None = None
