# https://www.geeksforgeeks.org/array-rotation/

def rotate(arr, d, n):
    d = d % n
    return arr[d:] + arr[:d]
