keybord = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./"
]

direction = input()
typed_massge = input()

character_position = {}

for row in keybord:
    for idx , char in enumerate(row):
        character_position[char] = (row, idx)
        
corrected_massage = []

for i in typed_massge :
    row , idx = character_position[i]
    if direction == 'R':
        corrected_massage.append(row[idx-1])
    elif direction == 'L':
        corrected_massage.append(row[idx+1 % len(row)])
    
print(''.join(corrected_massage))        
                    
                    