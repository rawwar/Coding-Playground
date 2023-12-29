def firstDuplicateValue(array):
    # Write your code here.
    for idx, each in enumerate(array):
        each_ = abs(each)
        if array[each_ - 1] < 0:
            return each_
        else:
            array[each_ - 1] = -1 * array[each_ - 1]
    return -1