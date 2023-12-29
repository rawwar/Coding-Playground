def longestPeak(array):
    # Write your code here.
    longest_peak = 0
    i = 1
    while i < len(array) - 1:
        if array[i] <= array[i+1] or array[i] <= array[i-1]:
            i+=1
            continue
        l = i - 1
        r = i + 1
        while l > 0:
            if array[l] > array[l-1]:
                l -= 1
            else:
                break
        while r < len(array)-1:
            if array[r] > array[r+1]:
                r += 1
            else:
                break
        longest_peak = max(longest_peak, r - l + 1)
        i+= 1
    return longest_peak
    
            
            
            