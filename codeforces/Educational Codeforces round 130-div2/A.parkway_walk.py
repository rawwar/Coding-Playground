T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(max(0, sum(lst) - m))