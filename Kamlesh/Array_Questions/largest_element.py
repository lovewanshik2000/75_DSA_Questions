# Given an array, find the largest element.

def largest_element(arr):
    large = arr[0]
    for i in arr:
        if i > large:
            large = i
    return large

# arr = [3, 7, 2, 9, 5]
# arr = [-5,-2,-8]
# arr = [10]
arr = [12, 45, 23, 67, 34]
print(f"Largest Element in given array {arr} is : ", largest_element(arr))