# Remove All Occurrences of a Specific Item



def remove_occurrences(input_list, item):
    l = []
    
    for i in input_list:
        if i != item:
            l.append(i)
    
    return l


print(remove_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10, 1], 1)) 