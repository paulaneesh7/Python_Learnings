# Append new string in the middle of a given string

def append_string(str1, str2):
    middle_index = int(len(str1)/2)
    new_str = str1[middle_index:] + str2 + str1[:middle_index]

    return new_str


print(append_string("hello", "world"))