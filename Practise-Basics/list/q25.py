# Find the first occurrence of a specific value in a list and replace it with a new value.


def replace_first_occurrence(input_list, target_item, new_item):
    
    if target_item in input_list:
        index = input_list.index(target_item)
        input_list[index] = new_item
    return input_list


print(replace_first_occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, "new_item"))