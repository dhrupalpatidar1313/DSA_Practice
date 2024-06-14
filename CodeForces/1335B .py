for _ in range(int(input())):
    
    n , a , b = map(int , input().split())
    
    pattern = ''.join(chr(ord('a') + i % b) for i in range(a))
    
    extend_pattern = (pattern * ((n // a ) + 1 ))[:n]
    
    print(extend_pattern)