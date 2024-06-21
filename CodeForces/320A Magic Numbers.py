n = input()
if len(n) == n.count('1') or '14' == n or '144' == n:
    print('YES')
elif n.count('14') == int(len(n)/2) and len(n) > 3 :
    print('YES')
elif n.count('144') == int(len(n)/3) and len(n) > 5:
    print('YES')
elif n.count('1') + n.count('14') + n.count('144') == len(n):
    print('YES')
else:
    print('NO')