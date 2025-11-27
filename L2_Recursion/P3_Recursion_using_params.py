# Problem: Print the value of x, N times

def func(x,N):
    if N==0:
        return
    print(N, "time Value of x: ",x)
    func(x,N-1)


func(15,4)


"""
# Recursion Tree:

Func(15,4)
   || Print 15
   ||
Func(15,3)   
   || Print 15
   ||
Func(15,2)
   || Print 15
   ||
Func(15,1)
   || Print 15
   ||
Func(15,0) 
   ||
   ||
Return
"""