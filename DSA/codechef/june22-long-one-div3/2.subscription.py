from math import ceil
N = int(input())

for _ in range(N):
    N, X = map(int, input().split())
    print(ceil(N/6) * X)

