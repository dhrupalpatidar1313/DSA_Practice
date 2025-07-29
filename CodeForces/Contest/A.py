t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    min_seconds = n + (n-1) * (k-1)
    print(min_seconds)