

# To save memory, we can use generator comprehensions instead of list comprehensions.
# A generator comprehension is similar to a list comprehension, but it uses parentheses instead of square brackets. 
# It returns a generator object that can be iterated over, but it does not create the entire list in memory at once.



daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# we could have done this with a list comprehension, but it would create a list in memory that we don't need:
# total_cups = sum([sale for sale in daily_sales if sale > 7])
# Also with a parenthesis, we can use the built-in sum function directly on the generator expression, which is more efficient.
total_cups = sum(sale for sale in daily_sales if sale > 7)


print(total_cups)