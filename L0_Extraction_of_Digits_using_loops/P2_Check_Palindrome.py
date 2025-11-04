# Write a program to check given number is palindrome or not

def checkPalindrome(n):
    num = n
    result = 0
    while num>0:
        last_digit = num%10
        result = (result*10) + last_digit
        num = num//10
    if result == n:
        return True
    else:
        return False
    
n = 121     #True
# n = 122     # False
res = checkPalindrome(n)
print(f"Palindorm of given number {n} is : ", res)


# Time complexity: O(log10(N))
# Space Complexity: O(1)