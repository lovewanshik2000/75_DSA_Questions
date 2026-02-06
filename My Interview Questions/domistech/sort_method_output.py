"""
Docstring for My Interview Questions.domistech.sort_method_output
What is output of this code
"""

nums = [5,7,9,8]
nums2 = nums.sort()
print("Output: ",nums2)

"""
Output is None:

🤯 Why is the output None?

Because list.sort() does NOT return a new list.
It sorts the list in place and returns None.
"""

# Correct Way (If you want a new sorted list)
nums = [5,7,9,8]
nums2 = sorted(nums)

print("Sorted: ",nums2)  # [5, 7, 8, 9]
print("Original: ",nums)   # [5, 7, 9, 8] (original unchanged)

"""
Interview One-Liner

.sort() modifies the list in place and returns None, 
while sorted() returns a new sorted list without modifying the original.
"""