def solve(a: list,b: list,n: int):
    mp = [0]*n
    for i in range(n):
        mp[a[i]-1] = b[i]
    a.sort()
    print(*a , sep=" ")
    for i in a:
        print(mp[i-1] , end=' ')
    print()
    
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))
    solve(a , b , n)
    t -= 1    
    
    