n = int(input())
city_cod = list(map(int , input().split()))

start = city_cod[0]
end = city_cod[n-1]

for i in range(n):
    max_dis = max(abs(start - city_cod[i]) , abs(end - city_cod[i]))
    if i < n-1:
        min_dis = min(abs(city_cod[i+1] - city_cod[i]) , abs(city_cod[i] - city_cod[i-1]))
    if i == 0 :
        min_dis = abs(start - city_cod[i+1])
    elif i == n-1 :
        min_dis = abs(end - city_cod[i-1])
    print(f"{min_dis} {max_dis}")    
        