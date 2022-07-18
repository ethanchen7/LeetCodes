class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(r,c):
            
            queue = collections.deque([(r,c)])
            
            while queue:
                
                r, c = queue.popleft()
                if (r,c) not in visited:
                    visited.add((r,c))
                    
                    for x,y in directions:
                        newR, newC = r + x, c + y
                        if 0<=newR<rows and 0<=newC<cols and (newR, newC) not in visited and grid[newR][newC] == "1":
                            queue.append((newR,newC))
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands
                    