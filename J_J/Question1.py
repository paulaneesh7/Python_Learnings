

# Consider a list [1,4,5,6,9,1,2,3,4,7]. Find the longest consecuitive series of numbers eg: it has 4,5,6 and 1,2,3,4 but 1,2,3,4 is the solution

def longest_consecutive_series(lst):
    lst = sorted(lst)
    longest = []
    current = []
    for i in range(len(lst)-1):
        if lst[i] + 1 == lst[i+1]:
            current.append(lst[i])
        else:
            current.append(lst[i])
            if len(current) > len(longest):
                longest = current
            current = []
    return longest

lst = [1,4,5,6,9,1,2,3,4,7]
result = longest_consecutive_series(lst)
print(result)
