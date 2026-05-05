# Add new item to list after a specified item


def add_item_index(lst, index, item):
    l = []
    for i in range(len(lst)):
        if i == index:
            l.append(item)
            l.append(lst[i])
        else:
            l.append(lst[i])

    return l


print(add_item_index([10,20,30,40], 2, 50))