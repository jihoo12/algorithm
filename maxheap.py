import sys
import heapq
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    c=int(sys.stdin.readline())
    if c==0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr,-c)