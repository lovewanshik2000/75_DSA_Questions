# """
# Write a program to count frequency of m list of characters
# Constraint:
# 1. 'a'<=s[i]<='z'
# """

s = "abcsabcaddjaabbc"
m = ['d','a','y','c']

hash_list = [0]*26

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value-97
    hash_list[index] +=1
res = []
for i in m:
    ascii_value= ord(i)
    index = ascii_value - 97
    res.append(hash_list[index])

print(res)

# T O(n+m)

# ##############################################


k = "abcsabcaddjaabbc"
q,l = ['d','a','y','c'],[]

hash_map = {}

for i in k:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

print(hash_map)


for i in q:
    if i in hash_map:
        l.append(hash_map[i])
    else:
        l.append(0)

print(l)