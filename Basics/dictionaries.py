

chai_types = {"Masala": "Spicy", "Ginger": "Strong", "Lemon": "Sour", "Mint": "Fresh"}

# Accessing elements through keys
key1 = chai_types["Masala"]
key2 = chai_types["Ginger"]
key3 = chai_types.get("Lemon")

print("Keys: ", key1, key2, key3)

# Manipulating Value through key
chai_types["Masala"] = "Spicy and Aromatic"
print(chai_types)

# Looping through dictionary -> In Dictionary when we loop like this, we only get keys
for chai in chai_types:
    print(chai)

# Looping through dictionary -> In Dictionary when we loop like this, we get both keys and values
for key, value in chai_types.items():
    print(key, value)

#  Also can be done like this
for chai in chai_types:
    print(chai, chai_types[chai])

# Access keys and values
print(chai_types.keys())
print(chai_types.values())


# Adding keys and values in dictionary
chai_types["Tawa"] = "Roasted"
print(chai_types)

# Pop method in Dictionary
# chai_types.pop("Tawa")

# Delete from Dictionary
# del chai_types["Masala"]


# Copy Method
chai_types_copy = chai_types.copy()
print(chai_types_copy)

# Nested Dictionary (Also possible in List)
beverage_shop = {
    "chai": {
        "Masala": 50,
        "Ginger": 40,
        "Lemon": 45,
        "Mint": 55
    },

    "coffee": {
        "Black": 60,
        "Latte": 70,
        "Cappuccino": 80
    },

    "juice": {
        "Orange": 40,
        "Apple": 50,
        "Pineapple": 60
    }
}

print(beverage_shop["chai"]["Masala"])

# Dictionary comprehension
squared_num = {x: x**2 for x in range(10)}
print(squared_num)
squared_num.clear() # Clear all the elements from dictionary


# Creating Dictionary in different procedure
keys = ["Luffy", "Ichigo", "Naruto", "Natsu"]
default_value = "Universal"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)