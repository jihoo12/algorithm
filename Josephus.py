from collections import deque
trash = []
n,k = map(int,input().split())
arr = deque(range(1,n+1))
while arr:
    arr.rotate(-k+1)
    trash.append(arr.popleft())
print(f"<{', '.join(map(str, trash))}>")
