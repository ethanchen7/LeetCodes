class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        queue = deque()
        
        directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        
        if grid[0][0] == 0:
            queue.append((1,(0,0)))
            visited.add((0,0))
        
        while queue:
            dist, path = queue.popleft()
            r, c = path[0], path[1]
            if (r,c) == (rows-1, cols-1):
                return dist
            
            for x,y in directions:
                newR, newC = r + x, c + y
                
                if 0<=newR<rows and 0<=newC<cols and grid[newR][newC] == 0 and (newR, newC) not in visited:
                    queue.append((dist+1, (newR, newC)))
                    visited.add((newR, newC))
                    
        return -1