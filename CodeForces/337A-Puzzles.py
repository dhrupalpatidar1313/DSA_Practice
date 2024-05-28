import sys
n , m  = map(int , input().split())
nums: list = list(map(int , input().split()))
nums.sort()
min_diffe = float('inf')
for i in range(m - n + 1):
    curr_diffe = nums[i - 1 + n] - nums[i]
    if curr_diffe <= min_diffe:
        min_diffe = curr_diffe
print(min_diffe)        