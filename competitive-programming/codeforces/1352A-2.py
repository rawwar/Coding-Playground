T = int(input())

for _ in range(T):
    n = input()
    l = len(n)
    res = [str(int(i)*(10**(l-1-idx))) for idx,i in enumerate(n) if i!= "0"]
    print(len(res))
    print(" ".join(res))
        