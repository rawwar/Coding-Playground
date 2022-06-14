t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    pos = 3
    if a > b:
        pos-=1
    if a > c:
        pos -= 1
    if a > d:
        pos -= 1
    print(pos)