from collections import defaultdict, deque
def dfs(node):
    max_depth = 1
    stack = [(node, 1)]
    while stack:
        current, depth = stack.pop()
        max_depth = max(max_depth, depth)
        for subordinate in subordinates[current]:
            stack.append((subordinate, depth + 1))
    return max_depth

subordinates = defaultdict(list)
roots = []

n = int(input())
managers = []
for _ in range(n):
    managers.append(int(input()))
    
for i in range(n):
    if managers[i] == -1:
        roots.append(i)
    else:
        subordinates[managers[i] - 1].append(i)    
max_depth = 0
for root in roots:
    max_depth = max(max_depth, dfs(root))

print(max_depth)   