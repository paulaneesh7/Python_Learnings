

def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"The cost of {quantity} {item} chai is: {cost}")
    except KeyError:
        print(f"Sorry, we don't have {item} chai.")
    except TypeError:
        print(f"Quantity must be a number. You provided: {quantity}")


process_order("masala", 3)  # Should calculate and print the cost
process_order("unknown", 2)  # Should handle KeyError for unknown item
