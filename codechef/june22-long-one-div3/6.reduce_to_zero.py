N = int(input())

for _ in range(N):
    X, Y = map(int, input().split())
    if X <=0 or Y <=0:
        print(-1)
        continue
    flag = True
    count = 0
    if X > Y:
        X, Y = Y, X
    while(X < Y):
        X *= 2
        count += 1
    print( count + Y)        
        

            



