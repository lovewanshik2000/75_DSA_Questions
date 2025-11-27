# Print 1 to N using Head Recursion

def head_func(i,N):
    if i>N:
        return
    print(i)
    head_func(i+1, N)

print("Using head Recursion")
head_func(1,4)

# Print 1 to N using Tail Recursion

def tail_func(N):
    if N==0:
        return
    tail_func(N-1)
    print(N)

print("Using tail Recursion")
tail_func(4)


# Print N to 1 using Head Recursion
def func(N):
    if N==0:
        return
    print(N)
    func(N-1)

print("N to 1 Using Head Recursion")
func(4)

# Print N to 1 using Tail Recursion
def func(i,N):
    if i>N:
        return
    func(i+1, N)
    print(i)

print("N to 1 Using Tail Recursion")
func(1,4)