# def checkPalindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left<right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# # Calling function
# s = "racecar"
# print(checkPalindrome(s))   # Output: True

# TIME COMPLEXCITY: O(N/2) similar to O(n)
# SPACE COMPLEXCITY: O(1)

# ===============================================================
# Approach 2: Using Recursion
def isPalindrome(s, left, right):
    if left >= right:
         return True
    if s[left] != s[right]:
            return False
    return isPalindrome(s, left+1, right-1)


# Calling function
s = "MOAOM"
n = len(s)-1
print(isPalindrome(s,left=0,right=n))

# TIME COMPLEXCITY: O(N/2) similar to O(n)
# SPACE COMPLEXCITY: O(1)