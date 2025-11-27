# Find the sum of 1 to N number using functional recursion.

"""
Rule for write functional recursion:
1. Create a workflow.   : N + f(N-1)
2. Create Base Condition.   : N==1
"""

def f(N):
    if N==1:
        return 1
    return N + f(N-1)

result = f(10)
print("Result: ", result)


# Time: O(N)
# Space: O(N)   # Stack Space