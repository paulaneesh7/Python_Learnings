# Turn Every Item of a List into its Square (List Comprehension)


def square_list(input_list):
    l = []
    for i in input_list:
        el = i*i
        l.append(el)
    return l


print(square_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))