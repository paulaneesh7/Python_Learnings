def count_occurrences(nums):
    counts = {}
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    return counts


nums = [1, 4, 5, 6, 9, 1, 2, 3, 4, 7]
result = count_occurrences(nums)

for num, count in result.items():
    print(f"{num}: {count}")
