class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj_list = {i: [] for i in range(len(points))}
        
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2,y2 = points[j][0], points[j][1]
                dist = abs(x1-x2) + abs(y1-y2)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])
        
        res = 0
        minHeap = [[0,0]]
        visited = set()
        
        while len(visited) < len(points):
            
            distance, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            
            res += distance
            visited.add(point)
            for pt in adj_list[point]:
                heapq.heappush(minHeap, pt)
        
        return res