# def find_center(n, m, grid):
#     first_row , first_col  = -1 , -1
#     last_row , last_col = -1 , -1 
#     for  i in range(n):
#         for j in range(m):
#             if grid[i][j] == '#':
#                 if first_row == -1:
#                     first_row = i
#                     break
#         if first_row != -1 :
#            break         
#     for  i in reversed(range(n)):
#         for j in range(m):
#             if grid[i][j] == '#':
#                 if last_row == -1:
#                     last_row = i
#                     break
#         if last_row != -1:
#             break        
#     for  j in range(m):
#         for i in range(n):
#             if grid[i][j] == '#':
#                 if first_col == -1:
#                     first_col = j
#                     break
#         if first_col != -1 :
#             break        
#     for  j in reversed(range(m)):
#         for i in range(n):
#             if grid[i][j] == '#':
#                 if last_col == -1:
#                     last_col = j
#                     break
#         if last_col != -1:
#             break
        
#     first_row += 1            
#     first_col += 1            
#     last_row += 1            
#     last_col += 1 
    
#     print(f'{int(first_row + (last_row - first_row)/2)} {int(first_col + (last_col - first_col)/2)}')           

    

# t = int(input())
# results = []
# for _ in range(t):
#     n, m = map(int, input().split())
#     grid = [input().strip() for _ in range(n)]
#     find_center(n, m, grid)

print(type(float(int(input()))))