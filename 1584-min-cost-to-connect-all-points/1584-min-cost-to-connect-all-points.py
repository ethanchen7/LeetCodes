class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj_list = {i: [] for i in range(len(points))}
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                point1, point2 = points[i], points[j]
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                adj_list[i].append([distance, j])
                adj_list[j].append([distance, i])
                
        visited = set()
        
        heap = [[0,0]]
        result = 0
        
        while len(visited) < len(points):
            
            distance, node = heappop(heap)
            
            if node in visited:
                continue
            
            visited.add(node)
            result += distance
            for n in adj_list[node]:
                heappush(heap, n)
            
            
        return result