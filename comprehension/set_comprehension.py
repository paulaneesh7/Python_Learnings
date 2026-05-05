

favourite_numbers = {1, 2, 3, 4, 5}


# Create a new set that contains only the even numbers from the favourite_numbers set
even_numbers = {num for num in favourite_numbers if num % 2 == 0}


favourite_chai = [
    "Masala Chai",
    "Green Tea",
    "Black Tea",
    "Oolong Tea",
    "White Tea",
    "Herbal Tea",
    "Chai Latte",
    "Matcha Latte",
    "Chai Tea",
]


unique_chai = {chai for chai in favourite_chai if "Chai" in chai}


print(even_numbers)
print(unique_chai)



recipes = {
    "Masala Chai": ["Tea Leaves", "Milk", "Sugar", "Spices"],
    "Green Tea": ["Green Tea Leaves", "Water"],
    "Black Tea": ["Black Tea Leaves", "Water"],
    "Oolong Tea": ["Oolong Tea Leaves", "Water"],
    "White Tea": ["White Tea Leaves", "Water"],
    "Herbal Tea": ["Herbs", "Water"],
    "Chai Latte": ["Tea Leaves", "Milk", "Sugar", "Spices"],
    "Matcha Latte": ["Matcha Powder", "Milk", "Sugar"],
    "Chai Tea": ["Tea Leaves", "Milk", "Sugar", "Spices"]
}

# Create a new set that contains all the unique ingredients used in the chai recipes that contain the word "Tea"
chai_ingredients = {ingredient for recipe in recipes.values() for ingredient in recipe if "Tea" in ingredient}

print(chai_ingredients)