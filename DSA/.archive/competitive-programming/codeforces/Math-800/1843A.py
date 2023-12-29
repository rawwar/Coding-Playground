T = int(input())

for _ in range(T):
    l = input()
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst)
    if len(lst) > 3:
        res = 0
        l = 0
        r = 
    elif len(lst) == 3:
        print(lst[-1] + lst[-2] - lst[0])
    elif len(lst) == 2:
        print(lst[0] + lst[1])
    else:
        print(0)
    