n = int(input())

lst = list(map(int, input().split()))

l = 1

result = 0

while l < len(lst):
    if lst[l] < lst[l-1]:
        result += lst[l-1] - lst[l]
        lst[l] = lst[l-1]
    l+=1
print(result)
