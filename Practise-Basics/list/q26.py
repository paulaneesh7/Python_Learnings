"""
Write a Python function that takes a list of numbers and returns the second largest value. 
Ensure the function handles lists with duplicate values correctly (e.g., if the list is [10, 10, 9], 
the second largest is 9).

"""




def second_largest(input_list):
    
    sorted_list = sorted(set(input_list), reverse=True)
    
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]



print(second_largest([10, 10, 9, 8, 7, 6, 5]))