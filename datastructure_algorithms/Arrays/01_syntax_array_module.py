from array import *

# Create an array of integers
val = array('i', [1,2,3,4,5])


# Printing array elements
for i in range(len(val)):
    print(val[i], end=' ')
    
val.append(6)  # Adding an element to the array
print("\nAfter appending 6:")

# Enhanced Loop version
for i in val:
    print(i, sep='\n')
    
    
ch = array('w', ['a', 'b', 'c', 'd', 'e'])
print("\nArray of characters:")    

# Advanced printing of array elements
print([c for c in ch])



# Find type-code of array
print("\nType code of ch array:", ch.typecode)


# Reverse an array
val.reverse()
print("\nReversed array: ", [v for v in val])



a = array('i', [10, 20, 30, 40, 50])

# Inserting an element at a specific position
a.insert(2, 25)  # Insert 25 at index 2
print("\nArray after insertion: ", [x for x in a])


# Copying an array
b = array(a.typecode, a) 
print("\nCopied array: ", [y for y in b])

# Delete Index (Pop also works)
del a[3]  
a.pop(1)
print("\nArray after deletion: ", [x for x in a])


abc = val[2:5]

for i in range(len(abc)):
    print(abc[i], end=' ')