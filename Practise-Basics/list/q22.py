# Concatenate Two Lists Index-wise


def concatenate_list_indexwise(list1, list2):
    result = []
    for i in range(len(list1)):
        el = list1[i] + list2[i]
        result.append(el)
    
    return result


list1 = ["Py", "is", "awes"]
list2 = ["thon", " ", "ome"]


print(concatenate_list_indexwise(list1, list2))



# Another way to do this is by using the zip() function, which allows you to iterate over multiple lists 
# in parallel.


for i, j in zip(list1, list2):
    print(i + j, end=" ")