class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        
        queue = collections.deque()
        queue.append((1,(0,0)))
        visited = set()
        visited.add((0,0))
        
        while queue:
            
            dist, coord = queue.popleft()
            r, c = coord[0], coord[1]
            
            if (r,c) == (rows-1, cols-1):
                return dist
            
            for x,y in directions:
                newR, newC = r+x, c+y
                if 0<=newR<rows and 0<=newC<cols and (newR,newC) not in visited and grid[newR][newC] == 0:
    
                    queue.append((dist+1, (newR,newC)))
                    visited.add((newR,newC))
            
        return -1