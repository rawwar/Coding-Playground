n = int(input())

for i in range(1, n+1):
    total = i**2 * (i**2 -1) // 2
    attack_count = 4 * (i-1)*(i-2)
    print(total - attack_count)
