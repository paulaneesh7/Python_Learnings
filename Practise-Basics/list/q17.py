# Count Occurrences of an Item


def count_occurrences(input_list, item):
    count = 0
    for i in input_list:
        if i == item:
            count += 1
    return count


print(count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10, 1], 1))