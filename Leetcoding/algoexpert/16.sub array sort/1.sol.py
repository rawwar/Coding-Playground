def subarraySort(array):
    # Write your code here.
    min_out_of_order = float('inf')
    max_out_of_order = float('-inf')
    for i in range(len(array)):
        if i == 0:
            if array[i] > array[i+1]:
                min_out_of_order = min(min_out_of_order, array[i])
                max_out_of_order = max(max_out_of_order, array[i])
        elif i == len(array) - 1:
            if array[i] < array[i-1]:
                min_out_of_order = min(min_out_of_order, array[i])
                max_out_of_order = max(max_out_of_order, array[i])
        elif array[i] > array[i+1] or array[i] < array[i-1]:
                min_out_of_order = min(min_out_of_order, array[i])
                max_out_of_order = max(max_out_of_order, array[i])
    if min_out_of_order == float('inf'):
        return [-1, -1]

    l = 0
    while min_out_of_order >= array[l]:
        l+=1
    r = len(array) - 1
    while max_out_of_order <= array[r]:
        r -= 1
    return [l, r]
        
                
                
    
