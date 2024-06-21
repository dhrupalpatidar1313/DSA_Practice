t = int(input())
while(t != 0):
    x , n , m =map(int , input().split())
    
    for i in range(n):
        x = int((x/2) + 10)
    for j in range(m):
        x -= 10    
    if x<=0:
        print('YES')
    else:
        print('NO')
    t -= 1        