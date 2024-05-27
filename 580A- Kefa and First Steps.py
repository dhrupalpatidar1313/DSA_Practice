n = int(input())
nums = list(map(int,input().split()))
if n == 0:
    exit()
max_count = 1
curr_count = 1
for i in range(n-1):
    if nums[i+1] >= nums[i]:
        curr_count += 1
    else:
        if curr_count > max_count:
            max_count = curr_count
        curr_count = 1
if curr_count > max_count:
    max_count = curr_count        
print(max_count)                