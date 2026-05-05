# Arrange string characters such that lowercase letters should come first


def lowercase_arragement(str):
    lower = []
    upper = []

    for char in str:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
            
    s = ""
    
    for i in lower:
        s += i
        
    for j in upper:
        s += j
        
    return s


print(lowercase_arragement("HelLo"))
