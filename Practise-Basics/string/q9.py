# Find all occurrences of a substring in a given string by ignoring the case

def find_occurrences(main_string, sub_string):
    return main_string.count(sub_string)

# Example usage
print(find_occurrences("hello world", "o"))  # Output: 2


