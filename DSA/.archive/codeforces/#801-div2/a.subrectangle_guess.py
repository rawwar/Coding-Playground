import sys
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = []
    high = -1 * 10**9 -1
    loc = [0,0]
    for i in range(n):
        inp = input().split()
        tmp = []
        for j,jj in enumerate(inp):
            jj = int(jj)
            if jj > high:
                high = jj
                loc = [i,j]
    h = max(loc[0],n-1-loc[0]) + 1
    w = max(loc[1], m-1-loc[1]) + 1
    print(h*w)


    
        