a, b = input().split()
a, b = int(a), int(b)

print(f"{min(a, b)} {abs(a-b)//2}")