# Split List into Chunks of Size N

def split_list_into_chunks(lst, n):
    ans = []
    
    for i in range(0, len(lst), n):
        ans.append(lst[i:i+n])
        
    return ans


print(split_list_into_chunks([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [[1, 2, 3], [4, 5, 6], [7]]

