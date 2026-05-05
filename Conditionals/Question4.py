fruit_color = input("Enter the color of the fruit: ")
fruit = input("Enter the name of the fruit: ")


if fruit_color == "Green":
    print(f"The {fruit} is Unripe.")
elif fruit_color == "Yellow":
    print(f"The {fruit} is Ripe.")
elif fruit_color == "Brown":
    print(f"The {fruit} is Overripe.")
else:
    print(f"The color {fruit_color} of the {fruit} is not recognized.")
