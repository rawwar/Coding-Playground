n, k = input().split()
n, k = int(n), int(k)

rem = (2/5)*(240 - k)
l, r = 0, n
res = 0

while l <= r:
    j = (l + r+1)//2
    if j == res:
        break
    val = j*(j+1)
    if val < rem:
        res = j
        l = j+1
    elif val > rem:
        r = j - 1
    else:
        res = j
        break
print(res)
        
    