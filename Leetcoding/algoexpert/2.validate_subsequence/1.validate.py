def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    for each in array:
        if i == len(sequence):
            return True
        if sequence[i] == each:
            i += 1
    return i == len(sequence)
