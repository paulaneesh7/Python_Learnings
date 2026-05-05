orders = ["apple", "banana", "orange"]


def get_order(index):
    try:
        return orders[index]
    except IndexError:
        return f"Invalid index. Please provide a valid index between 0 and {len(orders) - 1}"
    


print(get_order(1))  # Should return "banana"
print(get_order(5))  # Should return an error message about invalid index