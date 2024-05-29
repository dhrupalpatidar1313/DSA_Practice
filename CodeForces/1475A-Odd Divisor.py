for i in range(int(input())):
    n = int(input())
    while n%2 == 0:
        n = n / 2
    if n == 1:
        print('No')
    else:
        print('Yes')    