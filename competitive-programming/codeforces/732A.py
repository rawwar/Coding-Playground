k, r = input().split()

k, r = int(k), int(r)

for i in range(1, 11):
    if k*i % 10 in [0, r]:
        print(i)
        break