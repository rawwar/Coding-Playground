from collections import Counter


T = int(input())

for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    c = Counter(lst)
    print(len(lst) - c.most_common()[0][1])
    
    