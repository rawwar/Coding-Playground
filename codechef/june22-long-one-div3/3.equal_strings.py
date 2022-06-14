N = int(input())

for _ in range(N):
    n = int(input())
    A = input()
    B = input()
    hm = []
    for i in range(n):
        if B[i] == A[i]:
            pass
        else:
            if B[i] in hm:
                continue
            hm.append(B[i])
    print(len(hm))