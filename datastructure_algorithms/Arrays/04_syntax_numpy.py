from numpy import *


arr = array([1, 2, 3, 4, 5, "a"])

for x in arr:
    print(x, end=' ')
    
    

# Generate 5 evenly spaced numbers between 0 and 10
val = linspace(0, 10, 5)
print("\nLinspace array: ", val)



# Multidimensional array
multi_arr = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nMultidimensional array:\n", multi_arr)


