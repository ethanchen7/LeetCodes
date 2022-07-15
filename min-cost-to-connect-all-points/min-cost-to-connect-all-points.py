class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj_list = {i: [] for i in range(len(points))}
        
        for i in range(len(points)):
            point1 = points[i]
            for j in range(i+1, len(points)):
                point2 = points[j]
                distance = self.getDistance(point1, point2)
                adj_list[i].append([distance, j])
                adj_list[j].append([distance, i])
        # print(adj_list)
        
        res = 0
        visited = set()
        minHeap = [[0,0]] # distance, point
        
        while len(visited) < len(points):
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            res += dist
            
            for neiDist, neighbor in adj_list[i]:
                heapq.heappush(minHeap,[neiDist,neighbor])
        
        return res
                
                
    
    def getDistance(self, one, two):
        total = abs(one[0]-two[0]) + abs(one[1]-two[1])
        return total