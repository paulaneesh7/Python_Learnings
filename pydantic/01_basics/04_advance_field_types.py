from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import re



class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Employee Name",
        examples="John Doe" 
    )
    dept: Optional[str] = 'General' # Optional field with default value 'General'
    salary: float = Field(
        ...,
        ge=10000, # ge -> greater than equal to, gt -> greater than, le -> less than equal to, lt -> less than
    )


class User(BaseModel):
    email: str = Field(
        ...,
        regex = r''
    )
    phone: str = Field(
        ..., 
        regex = r''
    )
    age: int = Field(
        ...,
        ge=0,
        le=50,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )

