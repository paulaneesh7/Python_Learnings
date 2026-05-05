# Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


def concatenate_lst_in_order(lst1, lst2):
    l = []

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            l.append(lst1[i]+" "+lst2[j])

    return l


print(concatenate_lst_in_order(["Hello ", "take "], ["Dear", "Sir"]))