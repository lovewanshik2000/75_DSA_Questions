# 4️⃣ Second Largest (Without sort/set)

def find_second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

print(find_second_largest([2,5,3,7,1,9,4,]))