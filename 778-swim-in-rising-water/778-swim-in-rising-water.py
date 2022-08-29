class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        N = len(grid)
        heap = [(grid[0][0], 0 ,0)]
        visited = set()
        visited.add((0,0))
        
        time = 0
        while heap:
            
            d, r, c = heappop(heap)
            time = max(time, d)
            
            if r == N - 1 and c == N - 1:
                return time
            
            for x, y in dirs:
                newR, newC = r + x, c + y
                if 0<=newR<N and 0<=newC<N and \
                (newR, newC) not in visited:
                    heappush(heap,(grid[newR][newC],newR, newC))
                    visited.add((newR, newC))
        
      
            
        
        