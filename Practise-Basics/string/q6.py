# Count all letters, digits, and special symbols from a given string


def count_all(str):
    
    letters = 0
    digits = 0
    specials = 0
    
    for char in str:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():  # Ignore spaces when counting special characters
            specials += 1
            
    return f"Letters: {letters}, Digits: {digits}, Symbols: {specials}"


# Alternative version using ternary operator
def count_all_ternary(str):
    letters = 0
    digits = 0
    specials = 0
    
    for char in str:
        # Using ternary operators to increment counters
        letters += 1 if char.isalpha() else 0
        digits += 1 if char.isdigit() else 0
        specials += 1 if (not char.isalpha() and not char.isdigit() and not char.isspace()) else 0
            
    return f"Letters: {letters}, Digits: {digits}, Symbols: {specials}"


# Test both functions
test_string = "Hello World! 123"
print("Original function:", count_all(test_string))
print("Ternary version:", count_all_ternary(test_string))
