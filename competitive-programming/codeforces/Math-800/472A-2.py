# using sieve of Sieve of Eratosthenes

def sieve(n):
    primes = [1 for i in range(n+1)]
    primes[0] = 0
    primes[1] = 0
    
    for i in range(n+1):
        if primes[i] == 1:
            for j in range(i*i, n+1, i):
                primes[j] = 0
    st = set()
    for idx, i in enumerate(primes):
        if i:
            st.add(idx)
    return st

primes = sieve(10**6)

n = int(input())

for i in range(4, n):
    if i in primes or n-i in primes:
        continue
    print(i, n-i)
    break

