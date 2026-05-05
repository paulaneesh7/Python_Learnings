

class OutOfIngredientsError(Exception):
    """Custom exception for when ingredients are out of stock."""
    pass



def make_chai(milk, sugar):
    if milk <= 0 or sugar <= 0:
        raise OutOfIngredientsError("Milk and sugar must be greater than zero.")
    print(f"Making chai with {milk}ml of milk and {sugar}g of sugar... Done!")


make_chai(200, 50)
make_chai(0, 50)