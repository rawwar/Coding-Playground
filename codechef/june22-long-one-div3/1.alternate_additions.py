N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    q = B-A

    if q%3 in [0, 1]:
        print("YES")
    else:
        print("NO")