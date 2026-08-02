# Find All Common Elements Between Three Lists


def find_all_common_elements(list1, list2, list3):
    common = set(list1) & set(list2) & set(list3)
    return list(common)


print(find_all_common_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5]))