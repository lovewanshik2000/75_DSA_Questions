arr = [1,2,3,4,5]
"""
Swap this list number 1 to 5 & 5 to 1.
"""
i = arr.index(1)
j = arr.index(5)

arr[i], arr[j] = arr[j], arr[i]

print(arr)


# ================== Using Loop ================
arr = [1, 2, 3, 4, 5]

pos1 = -1
pos5 = -1

# Find positions using loop
for i in range(len(arr)):
    if arr[i] == 1:
        pos1 = i
    elif arr[i] == 5:
        pos5 = i

# Swap after loop
if pos1 != -1 and pos5 != -1:
    arr[pos1], arr[pos5] = arr[pos5], arr[pos1]

print(arr)