import re
for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    i = 0
    
    while i <= len(s) - 3:
        if s[i:i+3] == 'pie' or s[i:i+3] == 'map':
            count += 1
            i += 2  # Skip the next two characters to avoid overlapping
        i += 1   
            
    print(count)                