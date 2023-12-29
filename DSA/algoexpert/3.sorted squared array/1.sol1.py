def sortedSquaredArray(array):
    # Write your code here.
    if not array:
        return []
    pos_arr = []
    neg_arr = []
    for each in array:
        if each < 0:
            neg_arr.append(each*each)
        else:
            pos_arr.append(each*each)
    neg_arr = neg_arr[::-1]
    res = []
    L = 0
    R = 0
    while L < len(pos_arr) and R < len(neg_arr):
        if pos_arr[L] < neg_arr[R]:
            res.append(pos_arr[L])
            L += 1
        elif pos_arr[L] > neg_arr[R]:
            res.append(neg_arr[R])
            R+=1
        else:
            res.append(pos_arr[L])
            res.append(neg_arr[R])
            L+=1
            R+=1
    while L < len(pos_arr):
        res.append(pos_arr[L])
        L+=1
    while R < len(neg_arr):
        res.append(neg_arr[R])
        R+=1
    return res
    
        
        
        
        
