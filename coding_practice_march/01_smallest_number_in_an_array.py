"""
Find the smallest element in an array
Problem Statement: Given an array, we have to find the smallest element in the array.
Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output: 0  
Explanation:
  0 is the smallest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}  
Output: 5  
Explanation:
  5 is the smallest element in the array.
"""

def find_smallest_element(arr):
    """
    Algorithm:
        1. Create a variable called min and initialize it with the value of the first element in the array.
        2. Use a for loop to iterate through the remaining elements in the array.
        3. In each iteration, compare the current element with the min variable.
        4. If the current element is less than the min value, update the min value with the current element's value.
        5. After completing the loop, print the min variable, which will hold the smallest value in the array.
    """
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum

# ar = [2, 5, 1, 3, 0]
ar = 8, 10, 5, 7, 9
print(find_smallest_element(ar))
