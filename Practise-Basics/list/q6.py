# Remove empty strings from the list of strings


def remove_empty_strings(lst):
    l = []
    for i in range(len(lst)):
        if lst[i] != "":
            l.append(lst[i])

    return l


print(remove_empty_strings(["Mike", "", "Emma", "Kelly", "", "Brad"]))