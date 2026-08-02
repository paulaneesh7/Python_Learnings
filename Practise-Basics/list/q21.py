# Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [num for num in nums if num % 2 == 0]

print(new_list)