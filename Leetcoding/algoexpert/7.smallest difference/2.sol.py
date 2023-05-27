def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    l = 0
    r = 0
    smallest = float('inf')
    current = float('inf')
    smallest_pair = []
    while l < len(arrayOne) and r < len(arrayTwo):
        first_num = arrayOne[l]
        second_num = arrayTwo[r]
        if first_num < second_num:
            current = second_num - first_num
            l += 1
        elif first_num > second_num:
            current = first_num - second_num
            r += 1
        else:
            return [arrayOne[l], arrayTwo[r]]
        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
    return smallest_pair
            