def arrayOfProducts(array):
    # Write your code here.
    curr = 1
    res = []
    for each in array:
        res.append(curr)
        curr = curr * each
    curr = 1
    for i in range(len(array)-1, -1, -1):
        res[i] = res[i] * curr
        curr = curr * array[i]
    return res
