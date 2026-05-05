

menu = [
    "Pizza",
    "Pasta",
    "Salad",
    "Soup",
    "Sandwich",
    "Burger",
    "Sushi",
    "Steak",
    "Tacos",
    "Curry"
]

# Create a new list that contains only the items from the menu that start with the letter 'S'
s_items = [item for item in menu if item.startswith('S')]


print(s_items)
    

lst = [len(i) for i in menu if len(i) > 5]
print(lst)