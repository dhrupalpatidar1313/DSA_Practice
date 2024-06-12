k = int(input())
year = list(map(int , input().split()))

if sum(year) < k :
    print(-1)

year.sort(reverse=True)
sum = 0
count = 0
for i in year:
    if sum >= k :
        print(count)
        exit()
    sum += i
    count += 1
if sum == k :
    print(count)    