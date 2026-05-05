from pydantic import BaseModel, Field, field_validator, model_validator
from typing import List, Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str



# User contains reference of the Address mode
class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street = "123",
    city = "Shillong",
    postal_code = "1000001"
)

user = User(
    id=1,
    name="John",
    address=address
)



# We can create it this way as well
user_data = {
    "id": 1,
    "name": "John",
    "address": {
        "street": "347",
        "city": "Melbourne",
        "postal_code": "200345"
    }
}


user = User(**user_data)
print(user)