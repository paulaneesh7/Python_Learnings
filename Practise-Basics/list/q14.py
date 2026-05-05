# Accessing nested elements of a list


lsts = [[1, 2], [3, 4, 5], [6, 7]]

def access_nested_element(lsts, element=5):
    for lst in lsts:
        for i in lst:
            if element == i:
                print(f"Element {element} found inside {lst} at index: {i}")
                
    print(f"Element {element} was not found")
    
    

access_nested_element(lsts, 4)