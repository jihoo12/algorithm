n = int(input())
total = int(input())
num_list = list(map(int, input().split()))


num_list.sort()

start = 0
end = n - 1
count = 0

while start<end:
    
    s = num_list[start] + num_list[end]
    
    if s > total:
        e -= 1
    elif s < total:
        start += 1
    else:
        count += 1
        start += 1
        end -= 1
        
print(count)