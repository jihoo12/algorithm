from collections import deque
trash = []
n = int(input())
arr = deque(range(n,0,-1))
while len(arr)>1:
    trash.append(arr.pop())
    arr.rotate(1)
print(*arr)