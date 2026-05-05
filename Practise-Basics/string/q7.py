# Create a mixed String using the following rules

# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
# Any leftover chars go at the end of the result.


def mix_string(s1, s2):
    check_len = True if len(s1) > len(s2) else False
    
    s = ""
    
    
    if check_len:
        for i in range(len(s1)):
            s += s1[i] + s2[len(s2)-i-1]
    else:
        for i in range(len(s2)):
            s += s1[i] + s2[len(s1)-i-1]
            
    return s

print(mix_string("abcde", "12345"))