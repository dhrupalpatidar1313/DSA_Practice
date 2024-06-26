def mini_steps(number):
    n = len(number)
    
    min_step = float('inf')
    
    divisible_pairs = ['00','25', '50', '75']
    """_summary_

    Returns:
        _type_: _description_
    """    
    for pair in divisible_pairs:
        pos2 = -1
        pos1 = -1
        
        for i in range(n-1 , -1 , -1):
            if number[i] == pair[1]:
                pos2 = i
                break
        if pos2 == -1 :
            continue    
        
        for i in range(pos2 -1 , -1 , -1):
            if number[i] == pair[0]:
                pos1 = i
                break
        if pos1 == -1 :
            continue
        
        steps = (n -pos2 - 1) + (pos2 - pos1 - 1)        
        min_step = min(min_step , steps)
        
    return min_step    

for _ in range(int(input())):
    number = input()
    print(mini_steps(number))
    
    