n = int(input())

count = 0

while n >=5:
    res = n // 5
    count += res
    n = n//5
print(count)
    