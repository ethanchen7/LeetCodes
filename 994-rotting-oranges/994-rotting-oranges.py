class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        time = 0
        fresh_oranges = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        while queue and fresh_oranges > 0:
            
            for _ in range(len(queue)):
                r, c = queue.popleft()

                visited.add((r,c))

                for x, y in [[-1,0],[1,0],[0,1],[0,-1]]:
                    newR, newC = r + x, y + c
                    if newR < 0 or newC < 0 or newR >= rows or newC >= cols or (newR, newC) in visited or \
                    grid[newR][newC] != 1:
                        continue
                    queue.append((newR, newC))
                    visited.add((newR, newC))
                    fresh_oranges -= 1
            
            time += 1
        
        return time if not fresh_oranges else -1