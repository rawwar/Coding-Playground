n = int(input())

total = n*(n+1) // 2

if total % 2 == 0:
    print("YES")
    req = total // 2
    lst = list(range(1, n+1))
    lst2 = []
    while req != 0:
        if req > lst[-1]:
            lst2.append(lst[-1])
            req -= lst[-1]
            lst.pop()
        else:
            if req in lst:
                lst2.append(req)
                lst.pop(lst.index(req))
                req = 0
    print(len(lst))
    print(" ".join(map(str,lst)))
    print(len(lst2))
    print(" ".join(map(str,lst2)))
else:
    print("NO")