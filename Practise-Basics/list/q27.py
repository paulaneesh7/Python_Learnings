# Find the Most Frequent Element


def find_most_frequent1(input_list):
    frequency = {}
    
    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    return max(frequency, key=frequency.get)


def find_most_frequent2(input_list):
    frequency = {}
    
    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
        
    most_frequent_item = None
    max_frequency = 0
    
    for item, count in frequency.items():
        if count > max_frequency:
            max_frequency = count
            most_frequent_item = item
    
    return most_frequent_item


print(find_most_frequent1([1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10, 1]))
print(find_most_frequent2([1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 10, 1]))