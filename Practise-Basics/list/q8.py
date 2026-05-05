# Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] 
# in such a way that it will look like the following list.


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]


def extend_nestedlst_addSublst(list1, sub_list):
    list1.append(sub_list)

    return list1


print(extend_nestedlst_addSublst(list1, sub_list))