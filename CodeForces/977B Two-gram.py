n = int(input())

s = input().strip()

tow_gram_count = {}

for i in range(n-1):
    two_gram = s[i : i+2]
    
    if two_gram in tow_gram_count:
        tow_gram_count[two_gram] += 1
    else :
        tow_gram_count[two_gram] = 1
        
most_fr = max(tow_gram_count , key=tow_gram_count.get)

print(most_fr) 
          
    