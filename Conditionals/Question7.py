

order_size = input("Enter the size you want to order: ")
extra_shot = input("Do you want an extra shot of espresso? ")

if extra_shot == "Yes":
    coffee = order_size + " coffee with an extra shot of espresso"
else:
    coffee = order_size + " coffee"

print(f"Your order is: {coffee}")