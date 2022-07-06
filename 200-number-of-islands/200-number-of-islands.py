class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                
        if not grid:
            return 0
        
        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(r,c):
            
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            
            while queue:
                r, c = queue.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for x, y in directions:
                    newR, newC = r + x, c + y
                    
                    if ((newR, newC) not in visited and
                       (0 <= newR < rows and 0 <= newC < cols) and
                        grid[newR][newC] == "1"
                       ):
                        queue.append((newR, newC))
                        visited.add((newR, newC))
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
    
        return islands