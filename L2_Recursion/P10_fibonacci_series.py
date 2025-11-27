def fibonacciSeries(n):
    if n==0 or n==1:
        return n
    return fibonacciSeries(n-1) + fibonacciSeries(n-2)

print(fibonacciSeries(9))

# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

# import sys
# print(sys.getrecursionlimit())