from array import *


arr = array('i', [])


n = int(input("Enter the number of elements you want to add: "))
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)
    
print("The array elements are: ", [x for x in arr])



