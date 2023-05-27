def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    for i in range(len(intervals)):
        if result:
            curr = sorted_intervals[i]
            prev = result[-1]
            if prev[-1] >= curr[0]:
                result[-1] = [prev[0], max(curr[-1], prev[-1])]
            else:
                result.append(sorted_intervals[i])
        else:
            result.append(sorted_intervals[i])
    return result
