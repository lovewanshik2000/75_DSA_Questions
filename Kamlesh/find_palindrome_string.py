"""
✅ 2. Check Palindrome String

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
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True



print(find_palindrome_string("abcba"))

print(find_palindrome_string("hello"))