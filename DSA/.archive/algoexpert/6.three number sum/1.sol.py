def threeNumberSum(array, targetSum):
    # Write your code here.
    res = []
    array.sort()
    for idx, each in enumerate(array):
        total = targetSum - each
        l = idx + 1
        r = len(array) - 1

        while l < r:
            lhs = array[l] + array[r]
            if lhs == total: 
                res.append([each, array[l], array[r]])
                l += 1
                r -= 1
            elif lhs < total:
                l += 1
            elif lhs > total:
                r -= 1
    return res