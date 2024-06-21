for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    max_len = 1
    count = 1

    for i in range(1,n):
        if a[i] - a[i-1] <= k:
            count += 1
        else :
            count = 1
        max_len = max(count , max_len)
        
    print(n - max_len)
