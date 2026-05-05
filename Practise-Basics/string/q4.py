# Create a new string made of the first, middle, and last characters of each input string

def string_build(str1, str2):
    new_str = str1[0] + str2[int(len(str2)/2)] + str1[-1]
    return new_str

print(string_build("hello", "world"))