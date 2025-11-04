# Write a program to check given number is Armstrong Number.
# n = 153

def checkArmstrongNumber(n):
    num = n
    total = 0
    nod = len(str(num))
    while num>0:
        last_digit = num%10
        total += last_digit**nod
        num = num//10

    if total == n:
        return f"Give number({n}) is Armstrong Number."
    else:
        return f"Give number({n}) is not Armstrong Number."
    

n = "153,123,534,435"
numbers = [int(x) for x in n.split(',')]
for i in numbers:
    res = checkArmstrongNumber(i)
    print(res)


# Time Complexity = O(log10(N))
# Space Complexity = O(1)

    
