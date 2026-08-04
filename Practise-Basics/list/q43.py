# Move All Zeros to the End (Maintaining Order)


def move_zeroes_to_end(nums):
    
    ans = []
    
    for x in nums:
        if x != 0:
            ans.append(x)
    
    for x in nums:
        if x == 0:
            ans.append(x)
            
    return ans



print(move_zeroes_to_end([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]