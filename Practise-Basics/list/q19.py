# Remove Empty Strings from a List of Strings


def remove_empty_strings(input_list):
    l = []
    
    for item in input_list:
        if item != "":
            l.append(item)
    
    return l


print(remove_empty_strings(["PHP", "Exercises", "", "Backend", "Python", ""]))



# Another method
names = ["Mike", "", "Emma", "Kelly", "", "Brad"]
classed_names = list(filter(None, names))

print(f"Classed Names: {classed_names}")