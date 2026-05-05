
def occurences(str, target):
    count = 0
    words = str.split()
    for word in words:
        if word == target:
            count += 1
    return count



str_x = "Emma is good developer. Emma is a writer"
print(occurences(str_x, "Emma"))


print(str_x.count("Emma"))