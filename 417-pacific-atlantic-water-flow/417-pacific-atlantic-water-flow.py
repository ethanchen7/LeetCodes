class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = [], []
        pacVisited, atlVisited = set(), set()
        
        # add all the pacific and atlantic sided nodes to their arrays for traversal
        
        for r in range(rows):
            pac.append((r,0)) #left side pacific
            atl.append((r, cols - 1)) # right side atlantic
        
        for c in range(cols):
            pac.append((0, c)) # top side pacific
            atl.append((rows - 1, c)) # bottom side atlantic
            
        def dfs(r,c,visited):
            
            visited.add((r,c))
            dirs = [[1,0], [-1,0], [0,1],[0, -1]]
            
            for di, dj in dirs:
                newR, newC = r + di, c + dj
                if ((0 <= newR < rows) and 
                    (0 <= newC < cols) and
                    heights[newR][newC] >= heights[r][c] and
                    (newR, newC) not in visited):
                    dfs(newR, newC, visited)
        
        for r,c in pac:
            dfs(r,c,pacVisited)
        
        for r,c in atl:
            dfs(r,c,atlVisited)
        
        return pacVisited & atlVisited # return the intersection of the two sets
        