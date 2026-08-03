# Remove Negative Numbers In-place


def remove_negatives(lst):
    for item in lst:
        if item < 0:
            lst.remove(item)
    return lst


print(remove_negatives([-1, 2, -3, 4, -5]))  # Output: [2, 4]