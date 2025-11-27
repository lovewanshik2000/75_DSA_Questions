# Write a program to find the factorial of a given number using recursion.

def factorial(N):
    if N==0 or N==1:
        return 1
    return N*factorial(N-1)

print(factorial(1))

# Time Complexity: O(N)
# Space Complexity: O(N)    Stack Space

# factorial using for loop:-
result =1
num = 5

for i in range(num + 1):
    if i==0 or i==1:
        result *= 1
    else:
        result *= i

print(result)