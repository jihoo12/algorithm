def fibonacci2(N):
    n = 1500000
    m = 1000000
    base = [0]*n
    base[0] = 0
    base[1] = 1
    for i in range(2,n):
        base[i] = (base[i-1]+base[i-2]) % m
    print(base[N % n])
N = int(input())
fibonacci2(N)
