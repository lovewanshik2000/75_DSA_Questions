# 👉 “Check if a string can become a palindrome after removing at most one character.”

def valid_palindrome(s):
    def is_pal(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            print(s[left], s[right])
            res = is_pal(left+1, right) or is_pal(left, right-1)
            
            return res
        left += 1
        right -= 1

    return True


# Test
s = "abca"
print(valid_palindrome(s))  # True