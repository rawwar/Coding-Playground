from sys import stdin, stdout

n, q = map(int, input().split())

p  = [i for i in stdin.readline().split()]
p.sort()
for _ in range(q):
    x, y = map(int, input().split())
    count = 0
    for i in  p[n-x:n-y+1]:
        count += int(i)
    print(count)