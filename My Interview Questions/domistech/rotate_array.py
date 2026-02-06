"""
input = [1,2,3,4,6,7,8,9] 
Question rotate this arr from 4 to 8
output = [1,2,3,8,7,4,6,9]

"""
arr = [1,2,3,4,6,7,8,9]

start_val = 4
end_val = 8

start = arr.index(start_val)
end = arr.index(end_val)

sub = arr[start:end+1]          # [4,6,7,8]

# Custom rotation: last two elements first, then first two
rotated = sub[-1:-3:-1] + sub[0:2]

arr[start:end+1] = rotated

print(arr)