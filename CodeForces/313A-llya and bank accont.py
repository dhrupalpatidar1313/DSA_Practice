n = int(input())
last_del = n // 10

n_str = str(n)

if n < 0 :
    sec_last_del = int(n_str[:-2] + n_str[-1])
else :
    sec_last_del = int(n_str[:-2] + n_str[-1])
    
print(max(n , last_del , sec_last_del))        
