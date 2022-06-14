N = int(input())
for _ in range(N):
    inp = int(input())
    l = (inp-2)//2
    if l >0:
        print(int(l*(l+1)/2))
        continue
    print(0)

