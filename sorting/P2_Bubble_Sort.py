# write a program for Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-2, -1,-1):
        
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                print("++++++++++",i, j, j+1)
                arr[j], arr[j+1] == arr[j+1], arr[j]


nums = [2,5,8,3,9,1,4,7,10,6]
bubble_sort(nums)
print(nums)