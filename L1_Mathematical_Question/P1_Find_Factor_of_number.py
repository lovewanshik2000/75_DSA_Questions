# ************** 1 Brute force approch ************************
# n = 20
# res = []
# for i in range(1,n+1):
#     if n%i==0:
#         res.append(i)


# print(res)


# ********************* Best case approch **********************************
# n = 20 
# res = []
# for i in range(1, (n//2)+1):
#     if n%i==0:
#         res.append(i)
# res.append(n)

# print(res)




# ********************* Optimal solution approch ****************************
from math import sqrt
def findFactor(n):
    num = n
    res = []
    print(int(sqrt(num))+1)
    for i in range(1, int(sqrt(num))+1):
        if num%i == 0:
            res.append(i)
            if num//i != i:
                res.append(num//i)
            
    res.sort()
    return res
    
print("Squar root of given number: ", findFactor(120))