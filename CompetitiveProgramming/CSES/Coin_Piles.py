t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    a_ = 2*a -  b
    b_ = 2*b - a

    if a_ >= 0 and b_ >= 0 and a_%3 ==0 and b_%3 == 0:
        print("YES")
    else:
        print("NO")