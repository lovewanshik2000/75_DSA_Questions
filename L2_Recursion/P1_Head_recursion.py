count = 0
def func():
    global count
    if count == 4:
        return
    print(count,"Hello!, Kamlesh")
    count += 1
    func()

func()


# TC: O(N+1) similar to O(N)
# SC: O(N+1) similar to O(N)

"""
# Create Head Recursion Tree:

Func() if count=0
||      Print: Hello!, Kamlesh
||
||
func() if count=1
||      Print: Hello!, Kamlesh
||
||
func() if count=2
||      Print: Hello!, Kamlesh
||
||
func() if count=3
||      Print: Hello!, Kamlesh
||
||
func() if count=4
||
||
return
"""

"""
# Output: 
0 Hello!, Kamlesh
1 Hello!, Kamlesh
2 Hello!, Kamlesh
3 Hello!, Kamlesh
"""