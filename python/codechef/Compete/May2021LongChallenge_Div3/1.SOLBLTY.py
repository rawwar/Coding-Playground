N = int(input())
for _ in range(N):
    X, A, B = list(map(int, input().split()))
    print( 10 * ( A + (100 - X)*B))
