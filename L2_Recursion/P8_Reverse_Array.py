# Given arr = [5,7,3,2,6,1,5,9], left=2, right=5, Reverse the given array using given index
# Given arr = [5,7,3,2,6,1,5,9], left=0, right=7, Reverse the given array using given index

# ===============================================================
# Approach 1: Using Recursion
def revese(nums, left, right):
    if left >= right:
        return
    
    nums[left], nums[right] = nums[right], nums[left]
    revese(nums, left+1, right-1)

# Calling function
def reverseArray(arr, l, r):
    revese(arr,l,r)
    return arr

arr = [5,7,3,2,6,1,5,9]
l,r = 0,7
print(reverseArray(arr, l, r))

# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(n)  (due to recursive stack space)

# ===============================================================

# Approach 2: Using While Loop
arr = [5,7,3,2,6,1,5,9] 
left=2
right=5

def reverseArray(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverseArray(arr, left, right))

# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(1)
# ===============================================================

# Approach 3: Using For Loop
for i in range(left, right+1):
    if left >= right:
        break
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)

# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(1)
# ===============================================================

# Approach 4: Using Slicing
arr = [5,7,3,2,6,1,5,9]
left=2
right=5
arr[left:right+1] = arr[left:right+1][::-1]
print(arr)

# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(n)
# ===============================================================

# Approach 5: In-built Function reverse()
arr = [5,7,3,2,6,1,5,9]
left=2
right=5
sub_array = arr[left:right+1]
print(sub_array," before reverse")
sub_array.reverse()
print(sub_array," after reverse")
arr[left:right+1] = sub_array
print(arr)

# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(n)

# ===============================================================
# Approach 6: Complete Array Reverse using Slicing, In-built Function
arr = [5,7,3,2,6,1,5,9]
print("Original Array:", arr)
print("Slicing Reverse:",arr[::-1])
arr.reverse()
print("In-built Reverse:",arr)


# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(1) for in-built, O(n) for slicing
# ===============================================================
nums = [1,2,3,4,5,6,7]
n = len(nums)
for i in range(n):
    if i >=n:
        break
    nums[i], nums[n-1] = nums[n-1],nums[i]
    n -=1
    
print(nums)

# TIME COMPLEXCITY: O(n)
# SPACE COMPLEXCITY: O(1)
# ===============================================================