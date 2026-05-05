

def find_target_pairs(lst, target):

    l = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                l.append((lst[i], lst[j]))


    return l

def find_target_pairs2(lst, target):
    l = []
    s = set()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            el = lst[i] + lst[j]
            if el == target and (lst[i], lst[j]) not in s and (lst[j], lst[i]) not in s:
                l.append((lst[i], lst[j]))
                s.add((lst[i], lst[j]))

    return l

lst = [1, 4, 5, 6, 9, 1, 2, 3, 4, 7]
target = 10
result = find_target_pairs(lst, target)
print(result)


result = find_target_pairs2(lst, target)
print(result)
