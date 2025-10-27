"""
Problem: Find two numbers in the array that add up to a specific target.
"""

def two_sum(nums, target):
    seen = {}  # dictionary to store number:index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []  # if no pair found


# Driver Code
nums = [4, 7, 5, 15]
target = 9
result = two_sum(nums, target)
print(result)