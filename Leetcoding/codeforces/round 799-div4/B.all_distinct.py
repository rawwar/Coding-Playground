t = int(input())

for _ in range(t):
    l = int(input())
    lst = map(int, input().split())
    hm = {}
    for each in lst:
        if each in hm:
            hm[each] += 1
        else:
            hm[each] = 1
    count = 0
    even_count =0
    for i, j in hm.items():
        if j %2 == 0:
            even_count += 1
        else:
            count += 1
    if even_count % 2 == 0:
        count += even_count
    else:
        count += even_count-1        
    print(count)