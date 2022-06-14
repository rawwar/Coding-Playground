import math

N = int(input())

def factors(n):
    count = 0
    i = 1
    while(i <= math.sqrt(n)):
        if n%i == 0:
            if n//i == i:
                count +=1
            else:
                count += 2
        i+=1
    print(count)

for _ in range(N):
    A, B = map(int, input().split())
    factors(abs(B - A))


