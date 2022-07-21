class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(heights)
        cols = len(heights[0])
        
        pac = deque()
        atl = deque()
        
        for r in range(rows):
            pac.append((r,0))
            atl.append((r, cols - 1))
        
        for c in range(cols):
            pac.append((0, c))
            atl.append((rows - 1, c))
        
        pac_visited = set()
        atl_visited = set()
        
        def bfs(queue, visited):
            
            while queue:
                
                r, c = queue.popleft()
                visited.add((r,c))
                
                for x, y in dirs:
                    newR, newC = r + x, c + y
                    if 0<=newR<rows and 0<=newC<cols and heights[newR][newC] >= heights[r][c] and (newR, newC) not in visited:
                        queue.append((newR, newC))
        
        bfs(pac, pac_visited)
        bfs(atl, atl_visited)
        return pac_visited.intersection(atl_visited)