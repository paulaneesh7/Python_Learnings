

def check_brackets(expression):
    stack = []
    # Dictionary to match closing brackets with opening brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)  # Add opening brackets to the stack
        elif char in ')}]':
            if not stack or stack[-1] != matching_brackets[char]:
                return False  # If stack is empty or top doesn't match, return False
            stack.pop()  # Pop the matching opening bracket

    return stack == []  # If stack is empty, return True


# Test cases
print(check_brackets("[([])]"))  # True
print(check_brackets("[)[]]"))   # False
