t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    if len(lst) == 1:
        print("Mike")
        continue
    curr = 0
    count = 0
    while lst[curr] > 0:
        rem = 0