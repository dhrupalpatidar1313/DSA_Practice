t = int(input())
while(0< t < 1001):
     
    s = input()
    
    count_one = 0
    count_zero = 0
    
    for i in range(len(s)):
        if s[i] == '0':
            count_zero += 1
        else:
            count_one += 1
           
    total_turns = min(count_one , count_zero)
    
    if total_turns % 2 != 0:
        print('DA')
    else:
        print('NET')
    t -= 1                 