# fined the  second largest number in a list of unsorted integers.

# arr = [12, 35, 1, 10, 34, 2]
arr = [-55,-44,0, -1,-3]

def second_largest(numbers):
    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None

print(second_largest(arr))