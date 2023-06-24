T = int(input())

for _ in range(T):
    x, y, n = list(map(int, input().split()))

    nx = n%x
    if nx < y:
        print(max(0,n - nx - x + y))
    elif nx > y:
        print(n - (nx-y))
    else:
        print(n)