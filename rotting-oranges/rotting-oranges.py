class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        fresh_oranges = 0
        minutes_elapsed = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh_oranges > 0:
            
            for _ in range(len(queue)):
                orange = queue.popleft()
                r,c = orange[0], orange[1]
                
                for x,y in dirs:
                    newR, newC = r+x, c+y
                    if 0<=newR<rows and 0<=newC<cols and grid[newR][newC] == 1:
                        fresh_oranges -= 1
                        grid[newR][newC] = 2
                        queue.append((newR,newC))
            
            minutes_elapsed += 1
        
        return minutes_elapsed if fresh_oranges == 0 else -1