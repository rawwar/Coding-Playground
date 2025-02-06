from collections import deque

def grid_bfs(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
    
    def is_valid(row, col):
        return 0<= row < rows and 0 <= col < cols
    
    queue = deque([0, 0])
    visited = set([0, 0])
    
    while queue:
        row, col = queue.popleft()
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if is_valid(new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
    