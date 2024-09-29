t = int(input())

for _ in range(t):
    y, x = map(int, input().split())
    max_xy = max(x, y)  

    if max_xy %2 == 0:
        if y > x:
            print(max_xy**2 - x + 1)
        else:
            print( (max_xy-1)**2 + y)
    else:
        if y > x:
            print( (max_xy-1)**2 + x)
        else:
            print( max_xy**2 - y +1 )