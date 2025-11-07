"""
Write a program to count frequency of m
Constraint:
1. 1<=n[i]<=10
2. n can have 8^10 elements.
3. m can have 8^10 elements
"""
# ##################################### Using List based on condition ###########################
l = [5,3,2,2,1,5,5,7,5,10,1]
m = [10,111,1,9,5,67,2]

hash_list = [0]*11
for i in l:
    hash_list[i] += 1

res = []
for j in m:
    if j<1 or j>10:
        res.append(0)
    else:
        res.append(hash_list[j])

print(res)

# TIME COMPLEXCITY: O(m+n)
# SPACE COMPLEXCITY: O(1)

# ######################## Using Dictionary Recommended ##########################

l = [5,3,2,2,1,5,5,7,5,10,1]
m = [10,111,1,9,5,67,2]

hash_map = {}
result = []
for i in range(0,len(l)):
    if l[i] in hash_map:
        hash_map[l[i]] += 1
    else:
        hash_map[l[i]] = 1

for j in range(0, len(m)):
    if m[j] in hash_map:
        result.append(hash_map[m[j]])
    else:
        result.append(0)
print(hash_map)
print(result)