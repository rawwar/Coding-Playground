T = int(input())

for _ in range(T):
    n = int(input())
    if n%2 == 0:
        print(n//2 - 1)
    else:
        print(n//2)
