count = 0
def func(count):
    if count == 4:
        return
    count += 1
    func(count)
    print(count, "Hey!, Kamlesh")

func(count)

# TC: O(N+1) similar to O(N)
# SC: O(N+1) similar to O(N)

"""
# Create Tail Recursion Tree:

Func() if count=0
||
||      Print: Hey!, Kamlesh
||      ||
func() if count=1
||
||      Print: Hey!, Kamlesh
||      ||
func() if count=2
||
||      Print: Hey!, Kamlesh
||      ||
func() if count=3
||
||      Print: Hey!, Kamlesh
||      ||
func() if count=4
||      end func()
||      ||
return ==>
"""

"""
# Output: 
4 Hey!, Kamlesh
3 Hey!, Kamlesh
2 Hey!, Kamlesh
1 Hey!, Kamlesh
"""