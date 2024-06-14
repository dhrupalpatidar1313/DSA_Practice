for i in range(int(input())):
    check = True
    a , b , c = map(int , input().split())
    
    if (2 * b - c) % a == 0 and (2 * b - c) // a > 0:
        print("YES")
        check =False
    elif (a + c) % (2 * b) == 0 and (a + c) // (2 * b) > 0:
        print("YES")
        check =False
    elif (2 * b - a) % c == 0 and (2 * b - a) // c > 0:
        print("YES")
        check =False
    if check :
        print("NO")
