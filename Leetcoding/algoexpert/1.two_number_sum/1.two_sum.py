def twoNumberSum(array, targetSum):
    # Write your code here.
    hm = {}
    for idx, each in enumerate(array):
        if each in hm:
            return [each, hm[each]]
        else:
            hm[targetSum - each] = each
    return []
        
