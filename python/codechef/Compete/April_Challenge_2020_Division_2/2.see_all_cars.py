"""https://www.codechef.com/APRIL20B/problems/CARSELL"""

T = int(input())

for i in range(T):
    n = input()
    lst = list(map(int, input().split()))
    profit = 0
    lst =  sorted(lst)
    for each in range(len(lst)):
        # ind = lst.index(max(lst))
        temp = each*(-1) +  lst.pop()
        if temp < 0:
            continue
        else:
            profit += temp
    print(profit%1000000007)
