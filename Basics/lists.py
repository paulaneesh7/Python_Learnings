

tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)

# Indexing
el1 = tea_varities[0]
el2 = tea_varities[1]
print(el1, el2)
el3 = tea_varities[-1]
print(el3)

# Manipulate List
tea_varities[1] = "Ginger"
print(tea_varities)

# In 1st Index, both "Lemon" and "Dum Aloo" will be added
tea_varities[1:1] = ["Lemon", "Dum Aloo"]
print(tea_varities)

# Erasing elements from list
tea_varities[1:2] = []
print(tea_varities)

# Looping in list
for tea in tea_varities:
    print(tea, end=" -> ")


# Conditional Check
if "Oolong" in tea_varities:
    print("Oolong is available")


# Append Method
tea_varities.append("Tawa")
if "Tawa" in tea_varities:
    print("Tawa is available")


# Pop method - Deleting last element
tea_varities.pop()
print(tea_varities)

# Removing elements from list
tea_varities.remove("Ginger")
print(tea_varities)


# Insert Method
tea_varities.insert(1, "Ginger")
print(tea_varities)


# Copy Method
tea_varieties_copy = tea_varities # This will not create a copy, it will create a reference
tea_varieties_copy2 = tea_varities.copy() # This will create a copy
tea_varieties_copy3 = list(tea_varities) # This will create a copy

print(tea_varieties_copy)
print(tea_varieties_copy2)
print(tea_varieties_copy3)


# List Comprehension
squared_nums = [x**2 for x in range(10)]
print(squared_nums)

cube_nums = [x**3 for x in range(5)]
print(cube_nums)