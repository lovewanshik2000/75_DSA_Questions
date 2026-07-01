def mergeAlternately(word1, word2):
        result = []
        i = 0
        while i<len(word1) and i<len(word2):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        result.extend(word1[i:])
        result.extend(word2[i:])
        return "".join(result)

# Drive code
word1 = "abc"
word2 = "pqrst"

res = mergeAlternately(word1, word2)
print(res)