# 5️⃣ Remove Duplicates from List (Without set())

def remove_duplicate(arr):
    res = []
    for num in arr:
        if num not in res:
            res.append(num)
    return res

print(remove_duplicate([1,2,1,4,5,3,4]))