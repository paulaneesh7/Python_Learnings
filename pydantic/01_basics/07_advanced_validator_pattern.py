from pydantic import BaseModel, computed_properties, Field, field_validator, model_validator
from datetime import datetime

# Field Validator
class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError('Name must be capitalized')
        return v
    

# Field validator
class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
    


# Field Validator (mode='before')
class Product(BaseModel):
    price: str # $4.44


    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str): # if value is an instance of string
            return float(v. replace('$', '')) # then replace $ with nothing
        return v
    


# Model Validator
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError("end_date must be after start_date")