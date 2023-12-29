def sortedSquaredArray(array):
    # Write your code here.
    if not array:
        return []

    R = 0
    while R < len(array):
        if array[R] >=0:
            break
        R += 1
    L = R - 1
    res = []
    while L >= 0 and R < len(array):
        if -1*array[L] < array[R]:
            res.append(array[L]**2)
            L -= 1
        elif -1*array[L] > array[R]:
            res.append(array[R]**2)
            R += 1
        else:
            val = array[R]**2
            res.append(val)
            res.append(val)
            R += 1
            L -= 1
    while L >= 0:
        res.append(array[L]**2)
        L -= 1
    while R < len(array):
        res.append(array[R]**2)
        R+= 1
    return res
        
