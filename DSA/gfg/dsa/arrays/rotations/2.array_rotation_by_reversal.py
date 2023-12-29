# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/?ref=lbp

def reverse_array(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

def left_rotate(arr, d):
    n = len(arr)
    d = d % n
    if d == 0:
        return
    reverse_array(arr,0,d-1)
    reverse_array(arr,d,n-1)
    reverse_array(arr,)


def right_rotate(arr, d):
    n = len(arr)
    d = d % n
    if d == 0:
        return
    reverse_array(arr,n-d, n-1)
    reverse_array(arr,0, n-d-1)
    reverse_array(arr,0, n-1)

lst = [3,4,5,6,334,435,45,5436,543,4353,56]
right_rotate(lst, 10)
print(lst)