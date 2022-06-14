N = int(input())

for _ in range(N):
    n = int(input())
    mid = n//2 if n%2 == 0 else n//2 + 1
    lst = [mid]
    c = 1
    while True:
        if c==mid+1 or mid < c:
            break
        if n %2 != 0:
            if mid - c > 0:
                lst.append(mid-c)
            if mid + c <= n:
                lst.append(mid+c)
        else:
            if mid + c <= n:
                lst.append(mid+c)
            if mid - c > 0:
                lst.append(mid-c)
            
        c+=1
    print(" ".join(str(i) for i in lst))





