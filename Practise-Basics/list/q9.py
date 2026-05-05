# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. 
# Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]


def replace_list_item(lst, remove_item, item):
    l = []
    for i in range(len(lst)):
        if lst[i] == remove_item:
            l.append(item)
        else:
            l.append(lst[i])

    return l


print(replace_list_item(list1, 20, 200))