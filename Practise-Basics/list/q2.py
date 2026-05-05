# Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, 
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.


def concatenate_index_wise(list1, list2):
    result = []
    length1 = len(list1)
    length2 = len(list2)
    max_length = max(length1, length2)

    # Loop through the longer list's length
    for i in range(max_length):
        # Add elements from list1 if available
        if i < length1:
            result.append(list1[i])
        # Add elements from list2 if available
        if i < length2:
            result.append(list2[i])

    return result


# Test
list1 = ["A", "B", "C"]
list2 = ["1", "2", "3", "4", "5"]
print(concatenate_index_wise(list1, list2))
