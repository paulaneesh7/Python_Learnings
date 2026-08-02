# Remove Duplicates from List

def remove_duplicates(input_list):
    l = []
    
    for item in input_list:
        if item not in l:
            l.append(item)
            
    return l


print(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10, 1]))


duplicates = [10, 20, 10, 30, 40, 40, 20, 50]

# Method to remove duplicates while preserving order
unique_list = list(dict.fromkeys(duplicates))

print(f"Unique List: {unique_list}")