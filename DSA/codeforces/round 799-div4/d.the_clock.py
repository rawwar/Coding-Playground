t = int(input())

for _ in range(t):
    T, x = input.split()
    HH, MM = T.split(":")
    H,M = HH, MM
    while (f"{H}:{M}" < f"{HH}:{MM}"):

        if M > 59:
            M = M % 60
            H += 1
        if H >23:
            H = H%23


