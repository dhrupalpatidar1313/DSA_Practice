t = int(input())
while(t != 0):
    x , n , m =map(int , input().split())
    VA_total = 0
    LS_total = 0
    X_VA = x
    X_LS = x
    for i in range(n):
        X_VA = int(X_VA/2) + 10
    for j in range(m):
        X_LS = X_LS - 10
    # print(f'X_VA:{X_VA} , X_LS:{X_LS}')
    if X_VA <= 0 or X_LS <= 0:
        print('YES')
    elif (X_VA - (x - X_LS)) <= 0:
        print('YES')
    else:
        print('NO')         
    t -= 1  
        
    
         