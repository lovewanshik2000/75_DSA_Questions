# 1️⃣ Reverse a String (Without Slicing)

def reverse_string(s):
    res = ""
    for i in s:
        res = i + res
    return res

# Driver code
str1 = "hello"
result = reverse_string(str1)
print("Original String is: ", str1)
print("Reversed String is: ", result)

