class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj_list = {i: [] for i in range(len(points))}
        
        # building adjacency list of distance between edges for each node
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])
        
        # using a heap to sort the closest edges to always get the closest edge
        minHeap = [[0,0]]
        
        visited = set() # to avoid checking an edge we already checked
        result = 0
        
        while len(visited) < len(points):
            
            distance, node = heappop(minHeap)
            
            if node not in visited:
                visited.add(node)
                
                for d, v in adj_list[node]:
                    heappush(minHeap, [d, v]) 
            
                result += distance
        
        return result