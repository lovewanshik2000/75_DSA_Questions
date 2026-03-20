"""
Find Second Smallest and Second Largest Element in an array
Problem Statement: Given an array, find the second smallest and second largest element in the array. 
                   Print ‘-1’ in the event that either of them doesn’t exist.
Example 1:
Input: [1, 2, 4, 7, 7, 5]  

Output:
Second Smallest : 2  
Second Largest : 5  

Explanation: The elements are sorted as 1, 2, 4, 5, 7, 7.  
Hence, the second smallest element is 2, and the second largest element is 5.

Example 2:
Input: [1]  
Output:
Second Smallest : -1  
Second Largest : -1  

Explanation: Since there is only one element in the array, it is both the largest and smallest element.  
Therefore, there is no second smallest or second largest element present.
"""

def find_second_largest_or_smallest_element(arr):
    # ================= Brute Force Approch ===================
    # if len(arr) == 0 or len(arr) == 1:
    #     return f"Second smallest element: {-1} \nSecond largest element: {-1}"
    # arr.sort()
    # return f"Second smallest element: {arr[1]} \nSecond largest element: {arr[len(set(arr))-2]}"
    # """
    # Complexity Analysis
    #     Time Complexity: O(N log N), for sorting the array.
    #     Space Complexity: O(1), as we are using a constant amount of space for variables.
    # """

    # ================= Optimal Approach ===================
    if len(arr) < 2:
        print("Base case run: ")
        return f"Second smallest element: {-1} \nSecond largest element: {-1}"
    smallest = float('inf')
    second_smallest = float('inf')

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    # Handle edge cases
    
    if second_smallest == float('inf'):
        print("Edge cases run:")
        second_smallest = -1
    if second_largest == float('-inf'):
        second_largest = -1
    
    print("Output:")
    return f"Second smallest element: {second_smallest} \nSecond largest element: {second_largest}"

# Drive code:

# Base Case
# arr = [1]

# Input Case
arr = [1, 2, 4, 7, 7, 5]

# Edge Case
# arr = [float('inf'),float('-inf')]

print(find_second_largest_or_smallest_element(arr))