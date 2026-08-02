"""

Write a function that accepts a list and an integer n, returning a new list containing every nth element 
from the original, starting from the first element (index 0).

"""


def every_nth_element(input_list, n):
    return input_list[::n]


def every_nth_element_long_format(input_list, n):
    new_list = []
    for i in range(0, len(input_list), n):
        new_list.append(input_list[i])
    
    return new_list

print(every_nth_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(every_nth_element_long_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))