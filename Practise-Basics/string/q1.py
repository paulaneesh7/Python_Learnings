# Create a string made of the first, middle and last character

def string_build(str):
    return str[0] + str[int(len(str)/2)] + str[-1]


print(string_build("hello"))