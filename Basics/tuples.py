

tea_types = ("Black", "Green", "Oolong", "White")
print(tea_types)

# Indexing
el1 = tea_types[0]
el2 = tea_types[1]
print(el1, el2)

# Looping in tuple
for tea in tea_types:
    print(tea, end=" -> ")


# Conditional Check
if "Oolong" in tea_types:
    print("Oolong is available")


# Count Method
print(tea_types.count("Black"))

# Index Method
print(tea_types.index("Green"))


# Tuple Unpacking
tea1, tea2, tea3, tea4 = tea_types
print(tea1, tea2, tea3, tea4)


# Tuple with one element
tea_types_one = ("Black",)
print(tea_types_one)


# Tuple without parenthesis
tea_types_without_parenthesis = "Black", "Green", "Oolong", "White"
print(tea_types_without_parenthesis)

