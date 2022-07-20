class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row = len(rooms)
        cols = len(rooms[0])
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        
        queue = collections.deque()
        
        for r in range(row):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        step = 0
        while queue:
            
            
            for _ in range(len(queue)):
                r,c = queue.popleft()
                visited.add((r,c))
                
                if rooms[r][c] == pow(2,31) - 1:
                    rooms[r][c] = step
                
                for x,y in directions:
                    newR, newC = x + r, y + c
                    if 0<=newR<row and 0<=newC<cols and (newR, newC) not in visited and rooms[newR][newC] != -1:
                        queue.append((newR,newC))
            
            step += 1