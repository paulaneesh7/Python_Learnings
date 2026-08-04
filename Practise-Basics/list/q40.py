# Calculate Cumulative Sum (Prefix Sums)


def prefix_sum(nums):
    
    ans = []
    ans.append(nums[0])
    for i in range(1, len(nums)):
        ans.append(ans[i-1] + nums[i])
        
    return ans



print(prefix_sum([1, 2, 3, 4, 5]))  # Output: [1, 3, 6, 10, 15]