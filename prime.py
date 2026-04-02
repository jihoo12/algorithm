def prime(n):
    primes = [2]
    for i in range(3,n+1,2):
        isprime = 1
        for j in primes:
            if i%j==0:
                isprime = 0
        if isprime==1:
            if i not in primes:
                primes.append(i)
    return primes
print(prime(1000))