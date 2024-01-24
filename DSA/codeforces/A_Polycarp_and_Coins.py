T = int(input())

for _ in range(T):
    n = int(input())
    d = n%3
    ans = n//3
    if d == 0:
        print(ans, ans)
    elif d == 1:
        print(ans+1, ans)
    else:
        print(ans, ans+1)