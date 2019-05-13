
def is_prime(num):
    if num<1:return False
    if num <=3: return True
    if num%2==0 or num%3==0: return False
    for i in range(5,num):
        if i*i>num:
            break
        if num%i ==0 or num%(i+2)==0: return False
    return True

def are_sexy_primes(a, b):
    return is_prime(a) and is_prime(b)

print(are_sexy_primes(5,11))