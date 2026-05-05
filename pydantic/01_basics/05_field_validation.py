from pydantic import BaseModel, field_validator, model_validator

# Field Validator
class User(BaseModel):
    username: str

    # Just to validate particular field(s)
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return v


# Model Validator
class SignupData(BaseModel):
    password: str
    confirm_password: str

    # This is to validate the entire model or class
    # mode='after' means it will validate the model after all other validators are done with their job
    # If field_validators are present then those will validate first before this one starts, there are many other modes available
    @model_validator(mode='after')
    def password_match(vls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values
