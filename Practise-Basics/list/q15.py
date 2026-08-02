# Find the longest string in a list



def longest_string(words):
    l = 0
    
    s = ""
    for word in words:
        if len(word) > l:
            s = word
            l = len(word)
    return s



print(longest_string(["PHP", "Exercises", "Backend", "Python"]))