t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    initial_sum = sum(arr)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
    
    for __ in range(q):
        l, r, k = map(int, input().split())
        range_sum = prefix_sums[r] - prefix_sums[l - 1]
        new_sum = initial_sum - range_sum + (r - l + 1) * k
        if new_sum % 2 != 0:
            print("YES")
        else:
            print("NO")
