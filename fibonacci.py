def makef():
    f = [0,1]
    return f
def add(f,n):
    f.append(f[n]+f[n+1])
    return f
def fibonacci(n):
    f=makef()
    for i in range(n):
        f=add(f,i)
    return f
n = int(input())
r= fibonacci(n)
print(r)