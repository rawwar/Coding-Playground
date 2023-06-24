n = int(input())
lst = list(map(int, input().split()))
 
print(100*sum([i/100 for i in lst]) / len(lst)) 