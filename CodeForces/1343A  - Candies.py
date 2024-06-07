for i in range(int(input())):
    n = int(input())
    for j in range(2 , int(10e9)):
        den = pow(2 , j ) -1
        if(n%den == 0):
            print(int(n/den))
            break
            exit()
            
            