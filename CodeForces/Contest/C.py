import sys
input = sys.stdin.read

def query(i, j):
    print(f"? {i} {j}")
    sys.stdout.flush()
    return int(input())

def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        # Binary search for row
        low, high = 1, n
        best_row = -1
        while low <= high:
            mid = (low + high) // 2
            response = query(mid, 1)
            if response == 0:
                best_row = mid
                break
            elif response < n - mid + 1:
                low = mid + 1
            else:
                high = mid - 1
        
        # Binary search for column
        i0 = best_row
        low, high = 1, m
        best_col = -1
        while low <= high:
            mid = (low + high) // 2
            response = query(i0, mid)
            if response == 0:
                best_col = mid
                break
            elif response < m - mid + 1:
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(f"! {i0} {best_col}")
    
    print("\n".join(results))
    sys.stdout.flush()

solve()