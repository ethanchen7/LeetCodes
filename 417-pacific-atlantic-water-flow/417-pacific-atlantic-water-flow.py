class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        pacQ = []
        atlQ = []
        
        pacVisited = set()
        atlVisited = set()
        
        for r in range(rows):
            pacQ.append((r,0))
            atlQ.append((r, cols - 1))
        
        for c in range(cols):
            pacQ.append((0, c))
            atlQ.append((rows - 1, c))
                
        def dfs(r, c, visited):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited:
                return
            
            visited.add((r,c))
            for x, y in dirs:
                newR, newC = r + x, c + y
                if 0<=newR<rows and 0<=newC<cols and heights[newR][newC] >= heights[r][c] and (newR, newC) not in visited:
                    dfs(newR, newC, visited)
        
        for r, c in pacQ:
            if (r,c) not in pacVisited:
                dfs(r,c, pacVisited)
        
        for r, c in atlQ:
            if (r,c) not in atlVisited:
                dfs(r,c, atlVisited)
        
        return pacVisited.intersection(atlVisited)