def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    l = 0
    r = 0
    min_val = None
    min_keys = [0, 0]
    while l < len(arrayOne) and r < len(arrayTwo):
        diff = abs(arrayTwo[r] - arrayOne[l])
        if min_val is None:
            min_val = diff
            min_keys = [arrayOne[l], arrayTwo[r]]
        else:
            if min_val > diff:
                min_val = diff
                min_keys= [arrayOne[l], arrayTwo[r]]
        if l + 1 < len(arrayOne) and arrayOne[l+1] < arrayTwo[r]:
            l += 1
        elif r + 1 < len(arrayTwo) and arrayTwo[r+1] < arrayOne[l]:
            r += 1
        else:
            if l+1 < len(arrayOne) and r+1 < len(arrayTwo):
                if arrayOne[l+1] < arrayTwo[r+1]:
                    l +=1
                else:
                    r+= 1
            elif l+1 < len(arrayOne):
                 l += 1
            elif r+1 < len(arrayTwo):
                r += 1
            else:
                break
    return min_keys

arr1 =  [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530]
arr2 = [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]
print(smallestDifference(arr1, arr2))