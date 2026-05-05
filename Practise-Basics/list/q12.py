# Combine 2 lists

def combine_lst(lst_A, lst_B):
    l = []
    
    for item in lst_A:
        l.append(item)
        
    for item in lst_B:
        l.append(item)
        
    return l



print(combine_lst(["Physics", "Chemistry"], ["Maths", "Biology"]))