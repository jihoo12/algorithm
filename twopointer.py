import sys

N = int(input())
M = int(input())
arr = list(map(int, sys.stdin.readline().split()))
count = 0
current_sum = 0
end = 0
for start in range(N):
    while current_sum < M and end < N:
        current_sum += arr[end]
        end += 1
    if current_sum == M:
        count += 1
    current_sum -= arr[start]

print(count)