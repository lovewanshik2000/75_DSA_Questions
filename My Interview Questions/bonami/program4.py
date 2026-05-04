def char_index_map(s):
    result = {}

    for i, ch in enumerate(s):
        if ch not in result:
            result[ch] = []
        result[ch].append(i)

    return result


# Example
s = "abcaabbracdbrabc"
print(char_index_map(s))