N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
newarr = A+B
newarr.sort()
print(*newarr)