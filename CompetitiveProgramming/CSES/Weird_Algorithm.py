result = input()

n = int(result)

while n != 1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    result += f" {n}"

print(result) 