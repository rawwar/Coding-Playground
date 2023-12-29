T = int(input())

for _ in range(T):
    p = int(input())
    hun = p // 100
    ones = p % 100
    if hun >10 or ones > 10 or hun<0 or ones < 0:
        print(-1)
        continue
    if ones + hun > 10:
        print(-1)
        continue
    print(ones+hun)

