# Create a string made of the middle three characters

def string_build_middle(str):
    return str[int(len(str)/2)] + str[int(len(str)/2) + 1] + str[int(len(str)/2) + 2]


print(string_build_middle("hello"))
