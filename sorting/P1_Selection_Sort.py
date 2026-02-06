# Write a code for Selection Sort in ascending order
nums = [2,4,6,5,9,10,1,3]
def selection_sort_asc(nums):
    n = len(nums)
    for i in range(0,n):
        min_idx = i

        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

nums = [2,4,6,5,9,10,1,3]
print("Original list befor selection_sort_asc", nums)
selection_sort_asc(nums)
print("selection_sort_asc",nums)



print()


def selection_sort_desc(nums):
    n = len(nums)
    for i in range(0,n):
        min_idx = i

        for j in range(i+1, n):
            if nums[j] > nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    # (OR use this)
    # n = len(arr)
    # for i in range(n-1, -1,-1):
    #     min_idx = i
    #     for j in range(i-1, -1,-1):
    #         if arr[j] < arr[min_idx]:
    #             min_idx = j
    #     arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [2,4,6,5,9,10,1,3,100]
print("Original list befor selection_sort_desc", arr)
selection_sort_desc(arr)
print("selection_sort_desc" ,arr)

# Time complexity: O(n^2)
# Space Complexity: O(1)



