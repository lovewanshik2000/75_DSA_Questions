"""
✅ 1. First Non-Repeating Character

Problem Statement:
Given a string s, find the first non-repeating character and return its value. If it does not exist, return -1.

Example:
Input: s = "leetcode"
Output: l

Input: s = "aabb"
Output: -1
"""
# Start your code here
def first_non_repeating_char(string):
    mapper = {}
    for ch in string:
        mapper[ch] = mapper.get(ch, 0) + 1

    for j in range(len(mapper)):
        if mapper[string[j]] == 1:
            return string[j]
    return -1

# driver code
s = "leetcode"
# s = "aabb"
result = first_non_repeating_char(s)
print(result)

# End your code here
"""
Time Complexity	= O(n)
Space Complexity = O(n)

Interview Answer Structure:-

I will use a HashMap (dictionary) to count frequency in O(n) time, 
then iterate again to find first character with frequency 1. 
Overall complexity is O(n) time and O(n) space.
"""
