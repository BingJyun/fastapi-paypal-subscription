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
