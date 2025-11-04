# ########################## Method 1 #######################################


l = [1,2,3,2,2,1,3,4,5,1,44,5]
frequency_map = dict()

for i in range(0, len(l)):
    if l[i] in frequency_map:
        frequency_map[l[i]] += 1
    else:
        frequency_map[l[i]] = 1

print("Method 1 output:",frequency_map)

# Given x = 5
x = 5
print(frequency_map[x])

# TIME COMPLEXCITY : O(N)
# SPACE COMPLEXCITY : O(N)

# ########################## Method 2 #######################################
l2 = [1,2,3,2,2,1,3,4,5,1,44,5]
hash_map = {}
n = len(l2)
for i in range(0, n):
    hash_map[l2[i]] = hash_map.get(l2[i],0)+1
print("Method 2 output:", hash_map)


# TIME COMPLEXCITY : O(N)
# SPACE COMPLEXCITY : O(N)