# Rotate a List (Left or Right by k positions)
def rotate_list(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is larger than the list length
    return nums[-k:] + nums[:-k]



print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]