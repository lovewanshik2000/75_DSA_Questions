"""
Find the Largest element in an array
Problem Statement: Given an array, we have to find the largest element in the array.

Example 1:
Input:
 arr = [2, 5, 1, 3, 0]
Output: 5  
Explanation: 5 is the largest element in the array.

Example 2:
Input:
 arr = [8, 10, 5, 7, 9]
Output: 10  
Explanation: 10 is the largest element in the array.
"""

def find_largest_element(arr):
    """
    Algorithm:
        1. Create a variable called max and initialize it with the value of the first element in the array.
        2. Use a for loop to iterate through the rest of the elements in the array.
        3. In each iteration, compare the current element with the max variable.
        4. If the current element is greater than the max value, update the max value with the current element's value.
        5. After completing the loop, print the max variable, which will hold the largest value in the array.
    """
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

# arr = [2, 5, 1, 3, 0]

arr = [8, 10, 5, 7, 9]

print(f"Largest Element in given array is: {find_largest_element(arr)}")

"""
Complexity Analysis:
    1. Time Complexity: O(N), where N is the size of the array, as we are iterating through the array once.
    2. Space Complexity: O(1), as we are using a constant
"""