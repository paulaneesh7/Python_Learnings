

# Args is a tuple that stores all the arguments passed to the function
def sum_all(*args):
    return sum(args) # sum() is a built-in function that returns the sum of all the elements in a list

print(sum_all(1,2,3,4,5)) # 15
print(sum_all(1,2,3,4,5,6,7,8,9,10)) # 55
print(sum_all(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)) # 120