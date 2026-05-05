

chai = "Lemon Chai"
print(chai)

first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)

chai = "    Masala Chai    "

# Slicing and Indexing
num_list = "0123456789"
print(num_list[:3])
print(num_list[0:7:2]) # hoping of 1 number, if we write 0:7:3 then 2 number hoping

# Strip Method
print(chai.strip())

# Replace Method along with Strip
print(chai.replace("Masala", "Lemon").strip())

# Covert String to List
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))

# Find method
chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find("ai"))

# Cound method
chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

# Filling placeholder in string
chai_type = "Masala"
quantity = 2
order = "I order {} cups of {} chai"
print(order.format(quantity, chai_type))


# Join Method
chai_variety = ["Lemon", "Masala", "Ginger", "Mint"]
print("".join(chai_variety))
print(" ".join(chai_variety))

# Looping through string
chai = "Ginger Chai"
for letter in chai :
    print(letter)