
# Reverse a string

str = input("Enter a string: ")


def reverse_string(s):
    reversed_str = ""
    for c in s:
        reversed_str = c + reversed_str
    print("Reversed string: ", reversed_str)

reverse_string(str)
