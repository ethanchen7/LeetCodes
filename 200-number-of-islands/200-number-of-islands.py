class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        islands = 0
        
        def bfs(row, col):
            
            queue = collections.deque()
            visited.add((row, col))
            queue.append((row, col))
            
            while queue:
                
                (row, col) = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                
                
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if (newRow in range(rows) and 
                        newCol in range(cols) and 
                        grid[newRow][newCol] == "1" and 
                        (newRow, newCol) not in visited):
                        
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))
                        
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands