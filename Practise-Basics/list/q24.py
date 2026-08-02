# Find a specific item in a list and insert a new item immediately after it.


def insert_after_item(input_list, target_item, new_item):
    for i in range(len(input_list)):
        if input_list[i] == target_item:
            input_list.insert(i+1, new_item)
    return input_list


print(insert_after_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, "new_item"))