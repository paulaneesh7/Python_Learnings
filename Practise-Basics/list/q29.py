# Check if List is Palindrome


def isPalindrom(input_list):
    if input_list == input_list[::-1]:
        return True
    else:
        return False
    
    
def isPalindrome_long_format(input_list):
    reversd_list = reversed(input_list)
    if list(reversd_list) == input_list:
        return True
    else:
        return False
    
    
    
print(isPalindrom([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(isPalindrome_long_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
