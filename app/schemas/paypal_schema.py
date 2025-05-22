from pydantic import BaseModel

class Product(BaseModel):
    name: str
    type: str
    id: str | None = None
    description: str | None = None
    category: str | None = None
    image_url: str | None = None
    home_url: str | None = None