# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order 
# and items from list2 in reverse order.

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]


def list_order_reverse_order(lst1, lst2):
    lst2.reverse()
    return lst1, lst2


print(list_order_reverse_order([10, 20, 30, 40], [100, 200, 300, 400]))