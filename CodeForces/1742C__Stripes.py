import sys
input = sys.stdin.read
data = input().strip().split('\n')

index = 0
t = int(data[index].strip())
index += 1

results = []

for _ in range(t):
    while data[index].strip() == '':
        index += 1
    Box = []
    for i in range(8):
        Box.append(list(data[index].strip()))
        index += 1
    
    # Check for fully red rows
    red_found = False
    for i in range(8):
        if all(char == 'R' for char in Box[i]):
            results.append('R')
            red_found = True
            break
    
    # If no fully red row found, check for fully blue columns
    if not red_found:
        for i in range(8):
            col = [Box[row][i] for row in range(8)]
            if all(char == 'B' for char in col):
                results.append('B')
                break

# Print all results
for result in results:
    print(result)


