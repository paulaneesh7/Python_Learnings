# Extend Nested List by Adding a Sublist

def extend_nested(nested_list, item):
    for sublist in nested_list:
        sublist.append(item)
    return nested_list

# Test the function
data = [['apple', 'banana'], ['cherry', 'date']]
extra = "elderberry"
result = extend_nested(data, extra)

print(f"Updated Nested List: {result}")