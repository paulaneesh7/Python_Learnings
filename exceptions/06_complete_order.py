

class InvalidChaiError(Exception):
    """Custom exception for invalid chai flavors."""
    pass



def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 40, "cardamom": 30}
    try:
        if flavour not in menu:
            raise InvalidChaiError(f"Sorry, we don't have {flavour} chai.")
        if cups <= 0:
            raise ValueError("Number of cups must be greater than zero.")
        cost = menu[flavour] * cups
        print(f"The total cost for {cups} cups of {flavour} chai is: {cost}")
    except InvalidChaiError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our chai shop!")


bill("masala", 3)  # Should calculate and print the cost
bill("unknown", 2)  # Should raise InvalidChaiError and print the error