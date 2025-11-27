def func(res, i, N):
    if i > N:
        print("Given Natural Number Sum: ",res)
        return
    
    func(res+i, i+1, N)

func(0,1,4)

# Time: O(N)
# Space: O(N)   # Stack Space

