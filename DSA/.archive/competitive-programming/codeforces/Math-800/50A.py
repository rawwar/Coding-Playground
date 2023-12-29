n, m = input().split()
n, m = int(n), int(m)

if n < m:
    m, n = n, m

res = 0
if n == 1 or m == 1:
    res = n * m //2
else:
    res = n//2 * m + (n%2) * m//2

print(res)