n = int(input())

if n == 1:
    print("1")
elif n < 4:
    print("NO SOLUTION")
else:
    even = list(range(2, n+1, 2))
    odd = list(range(1, n+1, 2))
    print(" ".join(map(str, even+odd)))
    