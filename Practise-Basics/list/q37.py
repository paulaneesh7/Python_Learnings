# Concatenate Two Lists in a Specific Order

"""
Given two lists of strings, create a new list that contains every possible combination of elements from the first and second list, 
concatenated together.
"""


def concatenated_list(list1, list2):
    result = []
    
    for item in list1:
        for sub_item in list2:
            result.append(item + sub_item)
            
            
    return result




print(concatenated_list(['a', 'b'], ['1', '2']))  # Output: ['a1', 'a2', 'b1', 'b2']