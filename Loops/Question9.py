

# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.


items = ["apple", "banana", "orange", "apple", "mango"]
dict = {}

for item in items:
    dict[item] = dict.get(item, 0) + 1

for key, value in dict.items():
    if value > 1:
        print("Duplicates found", key)
        break
    else:
        print("No duplicates found")
        break