def moveElementToEnd(array, toMove):
    # Write your code here.
    l = 0
    r = len(array) - 1
    while l < r:
        if array[l] != toMove:
            l += 1
            continue
        if array[r] == toMove:
            r -= 1
            continue
        array[l], array[r] = array[r], array[l]
    return array
        
        
