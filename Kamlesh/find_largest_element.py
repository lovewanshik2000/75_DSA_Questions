# 3️⃣ Find Maximum Element (Without max())

def find_maximum(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum


arr = [1,5,3,6,4,8,0,12,2]
print(find_maximum(arr))
            