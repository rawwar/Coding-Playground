N = int(input())

count = 0
for _ in range(N):
    inp = input()
    if inp.count("1") >=2:
        count += 1
print(count)