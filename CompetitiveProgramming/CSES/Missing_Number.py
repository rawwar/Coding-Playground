n = int(input())

lst = list(map(int, input().split()))

total_sum = n * (n+1) //2 

lst_sum = sum(lst)

print(total_sum - lst_sum)