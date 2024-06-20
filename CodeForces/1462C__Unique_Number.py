for _ in range(int(input())):
    x = int(input())
    
    if x > 45:
        print(-1)
        continue
    sum = 0
    min_num = []
    i = 9
    while i > 0:
        if sum + i <=x:
            sum += i   
            min_num.append(i)
        i -= 1    
    if sum == x:
        min_num.sort()
        smallest_number = int(''.join(map(str, min_num)))
        print(smallest_number)
    else:
        print(-1)      