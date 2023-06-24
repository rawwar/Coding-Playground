l = int(input())
lst = map(int, input().split())

highest = 0
total = 0
for each in lst:
    highest = max(each, highest)
    total += each
print( (l*highest) - total)
