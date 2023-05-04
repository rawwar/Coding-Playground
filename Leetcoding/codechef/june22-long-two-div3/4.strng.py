def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x
def gcd_lst(lst):
    g = gcd(lst[0],lst[1])
    for i in lst[2:]:
        g = gcd(g,i)
    return g

def is_prime(n):
    if n <= 1:
        return False
    if n==2 or n==3:
        return True
    if n%2 == 0 or n %3 == 0:
        return False
    for i in range(5,int(n**0.5)):
        if n%i == 0 or n % (i+2) == 0:
            return False
    return True

# # print(is_prime(24))
T = int(input())

for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    
    # if len(set(lst)) == 1:
    #     print(len(lst))
    #     continue
    c = lst.count(1)
    if c > 1:
        print(0)
        continue
    
    no_primes = sum([1 if is_prime(i) else 0 for i in lst])

    if no_primes == 1:
        if gcd_lst(lst) == 1:
            print(1)
        else:
            print(len(lst))
    elif no_primes > 1:
        if gcd_lst == 1:
            print(0)
            continue
        print(len(lst))
    else:
        print(len(lst))

print(gcd_lst([1,1,1]))
