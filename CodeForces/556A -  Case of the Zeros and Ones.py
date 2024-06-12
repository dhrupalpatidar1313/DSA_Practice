n = int(input())
s = input().strip()

count_0 = s.count('0')
count_1 = s.count('1')

result = abs(count_0 - count_1)

print(result)
