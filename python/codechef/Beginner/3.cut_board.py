# cook your dish here
n = int(input())
for i in range(n):
    N,M = list(map(int,input().split()))
    print( (N-1)*(M-1))
