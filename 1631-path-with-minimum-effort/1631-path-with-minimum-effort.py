class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c,mid):
            visited.add((r,c))
            
            if r == rows-1 and c == cols-1:
                return True
            
            for x,y in directions:
                newR, newC = r + x, c + y
                if (0<=newR<rows and 0<=newC<cols) and (newR,newC) not in visited:
                    current_difference = abs(heights[newR][newC] - heights[r][c])
                    if current_difference <= mid:
                        if dfs(newR, newC, mid):
                            return True
        
        mn, mx = 0, 10**6
        while mn < mx:
            mid = (mn + mx) // 2
            visited = set()
            if dfs(0,0, mid):
                mx = mid
            else:
                mn = mid + 1
        
        return mn
            
                    