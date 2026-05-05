from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    total_price: float
    quantities: Dict[str, int] #str as key, int as value


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None # Optional field with default value None


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"Laptop": 1, "Mouse": 2, "keyboard": 1},
    "total_price": 1499.97
}

cart = Cart(**cart_data)

