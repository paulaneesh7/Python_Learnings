

age = int(input("Enter your age: "))
day = input("Enter day of the week: ")


price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("Your total price is: ", price)