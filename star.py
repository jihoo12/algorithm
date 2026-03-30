n=int(input())
for l in range(n-1):
    for j in range(2*n-l-1):
        print(" ",end="")
    for j in range(2*l):
        print("*",end="")
    print("*")
for i in range(n):
    for j in range(n+i):
        print(" ",end="")
    for j in range(n-i-1):
        print("*",end="")
    for k in range(n-i-1):
        print("*",end="")
    print("*")
