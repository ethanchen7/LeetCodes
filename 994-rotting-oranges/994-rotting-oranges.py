class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_oranges = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        
        queue = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                    
                if grid[r][c] == 1:
                    fresh_oranges += 1
        time = 0
        
        while queue and fresh_oranges > 0:
            
           

            for _ in range(len(queue)):
                r,c = queue.popleft()

                for x, y in dirs:
                    newR, newC = x + r, y + c
                    if (newR, newC) not in visited and 0<=newR<rows and 0<=newC<cols and grid[newR][newC] == 1:
                        visited.add((newR,newC))
                        queue.append((newR, newC))
                        fresh_oranges -= 1
            
            time += 1
        
        if fresh_oranges == 0:
            return time
        return -1
        
        