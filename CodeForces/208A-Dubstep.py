import re
s = input()
s = re.sub(r'(WUB)+' , ' ' , s)
print(s.strip())