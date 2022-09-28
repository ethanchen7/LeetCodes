class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        
        def bfs(r,c):
            
            distance = 0
            
            queue.append((r,c))
            visited = set()
            
            while queue:
                
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    visited.add((r,c))
                    rooms[r][c] = min(rooms[r][c], distance)

                    for x, y in [[-1,0],[1,0],[0,1],[0,-1]]:
                        newR, newC = r + x, y + c
                        if newR < 0 or newC < 0 or newR >= rows or newC >= cols or (newR, newC) in visited or \
                        rooms[newR][newC] == -1 or rooms[newR][newC] == 0:
                            continue
                        queue.append((newR, newC))
                        visited.add((newR, newC))
                
                distance += 1
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    bfs(r, c)