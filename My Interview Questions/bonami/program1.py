def count_duplicates(lst):
    freq = {}

    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    return list(freq.values())

# Test
print(count_duplicates([1,2,2,2,3,3,3]))
# [1,3,3]