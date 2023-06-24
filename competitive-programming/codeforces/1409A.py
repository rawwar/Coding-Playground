T = int(input())

for _ in range(T):
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
        continue
    diff = abs(a - b)
    if diff <= 10:
        print(1)
    else:
        res = diff//10
        if diff % 10 != 0:
            res += 1
        print(res)
    