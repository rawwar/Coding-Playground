T = int(input())
 
for _ in range(T):
    a, b = input().split()
    a, b = int(a), int(b)
    if a%b == 0:
        print(0)
    else:
        print(b - a%b)