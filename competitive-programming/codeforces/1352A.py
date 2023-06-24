T = int(input())

for _ in range(T):
    n = int(input())
    
    res = []
    den = 1
    while n > 0:
        if n%10 != 0:
            rem = n % 10
            res.append(str(rem*den))
        den *= 10
        n = n//10
    print(len(res))
    print(" ".join(res))
        