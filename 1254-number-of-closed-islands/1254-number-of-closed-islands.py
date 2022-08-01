class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        # an island is only closed if it doesn't go out of bounds
        # otherwise, by default we can just assume it is closed
        # in each bfs call, traverse every land neighbor until we can't anymore
        # as long as it doesn't go out of bounds, it's a valid closed island
        
        rows, cols = len(grid), len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        
        def bfs(r, c):
            
            queue = deque()
            queue.append((r,c))
            
            is_closed = True
            
            if (r,c) not in visited:
                visited.add((r,c))

                while queue:

                    r, c = queue.popleft()

                    for x, y in dirs:
                        newR, newC = x + r, y + c
                        if not (0<=newR<rows and 0<=newC<cols):
                            is_closed = False
                            continue
                        
                        if (newR, newC) not in visited and grid[newR][newC] == 0:
                            queue.append((newR, newC))
                            visited.add((newR, newC))
                
                if is_closed: return 1
                else: return 0
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 0:
                    count += bfs(r, c)
        
        return count