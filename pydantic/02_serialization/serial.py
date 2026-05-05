from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    # Because using datetime directly inside model isn't just right
    # So we have to configure it
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


user = User(
    id=1,
    name="John Doe",
    email="johndoe@gmail.com",
    is_active=False,
    created_at=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="34",
        city="Shangai",
        zip_code="343509"
    ),
    tags=["premium", "subscriber"]
)

print(user)


print("-"*50)


# How to use this above object now (always use model_dump() if you've nested models referencing inside model)
# model_dump() : here converts everything into a dict, check the print output with and without it
python_dict = user.model_dump()


print(python_dict)


print("-"*50)


# model_dump_json(): converts everything into json here (more usable)
json_str = user.model_dump_json()

print(json_str)