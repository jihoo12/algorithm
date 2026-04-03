def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a,b):
    data = a*b//gcd(a,b)
    return data
a,b=map(int,input().split())
print(int(gcd(a,b)))
print(int(lcm(a,b)))