# Find the Difference Between Two Lists

def difference_between_lists(list1, list2):
    return list(set(list1) - set(list2))



print(difference_between_lists([1, 2, 3, 4, 5], [4, 5, 6, 7]))  # Output: [1, 2, 3]