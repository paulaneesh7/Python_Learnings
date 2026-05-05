# Given a Python list, write a program to remove all occurrences of item 20.

def remove_all_occurences(lst, remove_item):
    l = []
    for i in range(len(lst)):
        if lst[i] == remove_item:
            pass
        else:
            l.append(lst[i])

    return l


print(remove_all_occurences([10,20,30,20,40,20,50], 20))