def fact(n):
    res = 1
    for i in range(n):
        if i > 0:
            res = res + res*i
    return res
num = 15
result = fact(num)        
print(result)

# Count Trainling Zeros
count = 0
while num>0:
    num = num//5
    print(num,"1111111111")
    count += num

print(count)
