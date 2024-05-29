nums = [1,2,3,2,5]
n = len(nums)   
if n == 0:
    print(1)
    exit()
    
# Step 1: Find the longest sequential prefix
max_prefix_length = 1
curr_prefix_length = 1
for i in range(1, n):
    if nums[i] == nums[i - 1] + 1:
        curr_prefix_length += 1
    else:
        break
max_prefix_length = max(max_prefix_length, curr_prefix_length)

# Calculate the sum of the longest sequential prefix
prefix_sum = sum(nums[:max_prefix_length])

# Step 2: Find the smallest integer greater than or equal to the prefix_sum that is missing from nums
missing_int = prefix_sum
num_set = set(nums)
while missing_int in num_set:
    missing_int += 1
    
print(missing_int)    