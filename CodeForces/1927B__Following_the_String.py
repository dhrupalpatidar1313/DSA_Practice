for _ in range(int(input())):
    n = int(input())
    trace = list(map(int , input().split()))
    res = ''
    count_of_char = [0] * 26
    
    for i in trace:
        char = chr(count_of_char.index(i) + ord('a'))
        res += char
        count_of_char[count_of_char.index(i)] += 1
    print(res)    
        