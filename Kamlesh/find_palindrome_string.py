"""
2️⃣ Check Palindrome (Without Slicing)

Problem Statement:
Given a string s, return True if it is a palindrome, otherwise return False.

Ignore case sensitivity.

Input: "madam"
Output: True

Input: "hello"
Output: False
"""

# def find_palindrome_string(s):
#     temp_s = s
#     if temp_s == s[::-1]:
#         return True
#     return False

def find_palindrome_string(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


inp = "abcba"
print(f"{inp} is Palindrome :{find_palindrome_string(inp)}")

inp2 = "hello"
print(f"{inp2} is Palindrome :{find_palindrome_string(inp2)}")