class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        
        def dfs(r,c):
            
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            
            return 1 + dfs(r-1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
    
        max_size = 0
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    size = dfs(r, c)
                    max_size = max(max_size, size)
        
        return max_size