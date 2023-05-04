T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    
    s = sorted(lst)
    
    if lst == s:
        print("YES")
        continue
    
    for i in range(len(s)-1,-1,-1):
        if s[i] == lst[i]:
            continue
        break
    if s[i]+s[i-1] <m:
        print("YES")
    else:
        print("NO")
    
    
        