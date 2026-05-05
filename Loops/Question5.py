

def first_non_repeating_character(s):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None  # Return None if no non-repeating character is found

# Input from the user
input_str = input("Enter a string: ")
result = first_non_repeating_character(input_str)

print(result)