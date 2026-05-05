from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True # Default value


product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)

product_two = Product(id=2, name="Smartphone", price=499.99, in_stock=False)

# This will give error because 'id' and 'price' are required fields
product_three = Product(name="keyboard")