# List to Dictionary Conversion


def lst_to_dict(lst1, lst2):
    new_dict = {}
    
    for item in range(len(lst1)):
        new_dict[lst1[item]] = lst2[item]
        
    return new_dict



print(lst_to_dict(['a', 'b', 'c'], [1, 2, 3]))  # Output: {'a': 1, 'b': 2, 'c': 3}