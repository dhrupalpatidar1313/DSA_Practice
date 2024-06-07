for i in range(int(input())):
    number = int(input())
    rem_2020 = int(number % 2020)
    rem_2021 = int(number % 2021)
    
    if rem_2020 == 0 or rem_2021 == 0:
        print('YES')
    else : 
        print('NO')    