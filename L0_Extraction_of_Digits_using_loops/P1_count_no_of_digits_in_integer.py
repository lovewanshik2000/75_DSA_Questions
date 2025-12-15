# ################## Using Loops ##################

# n = 7465
# num = n
# count = 0

# while num > 0:
#     count += 1
#     num = num//10

# print(f"number of digit in given {n} integer: ", count)

# Time Complexity: O(log10(N))
# Space Complexity: O(1)

# ################## Using Math library function:- log10() ##################
from math import *
def countDigits(n):
    return int(log10(n)+1)

num = 3272
result = countDigits(num)
print(f"number of digit in given {num} integer: ",result)

# Time Complexity: O(log10(N))
# Space Complexity: O(1)