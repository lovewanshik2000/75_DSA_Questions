# 6️⃣ Count Character Frequency (Without Counter)

def count_char_frequency(s):
    has_map = {}
    for i in s:
        if i in has_map:
            has_map[i] += 1
        else:
            has_map[i] = 1
    return has_map

print(count_char_frequency("hello"))
