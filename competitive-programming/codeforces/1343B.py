T = int(input())

for _ in range(T):
    n = int(input())
    if n%4 == 0 and n>=4:
        print("YES")
        result = [(i+1)*2 for i in range(n//2)]
        result2 = [2*i+1 for i in range(n//2)]
        result2[-1] += len(result)
        result = result + result2
        print(" ".join(str(i) for i in result))
    else:
        print("NO")