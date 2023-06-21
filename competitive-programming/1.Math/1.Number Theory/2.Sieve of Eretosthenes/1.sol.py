
def sieve(num):
    is_prime = [1 for i in range(num+1)]
    is_prime[0] = 0
    is_prime[1] = 0

    for i in range(int(num**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, num+1, i):
                is_prime[j] = 0
    return is_prime

num = 100
result = [idx for idx, i in enumerate(sieve(num)) if i==1]
print(result)
