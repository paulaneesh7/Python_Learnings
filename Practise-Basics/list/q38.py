# Flatten Nested List (2D to 1D)

def flatten_nested_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    
    return flat_list



print(flatten_nested_list([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]