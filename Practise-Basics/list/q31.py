# Write a function that takes a list of strings and an integer k. 
# The function should return a new list containing only the strings that have a length greater than or equal to k.



def filter_strings_by_length(lst_str, k):
    new_lst = [str for str in lst_str if len(str) >= k]
    return new_lst


print(filter_strings_by_length(["apple", "banana", "kiwi", "pear"], 5))  # Output: ['apple', 'banana']